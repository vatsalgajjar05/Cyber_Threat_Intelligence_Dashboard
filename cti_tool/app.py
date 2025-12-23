# --- shim for pkgutil.get_loader on newer Python versions ---
import pkgutil
import importlib.util

if not hasattr(pkgutil, "get_loader"):
    def _get_loader(name):
        try:
            spec = importlib.util.find_spec(name)
        except Exception:
            return None
        return spec.loader if spec else None
    pkgutil.get_loader = _get_loader
# --- end shim ---

from flask import Flask, render_template, jsonify, request, Response
from config import Config
from database.sqlite_db import (
    init_db,
    insert_ioc,
    fetch_all_iocs,
    fetch_trend_events
)
from services.virustotal import vt_lookup_ip
from services.abuseipdb import abuse_lookup_ip

import datetime
import logging
import requests
import sqlite3

# PDF generator (optional)
try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    # -------------------------
    # INIT DB
    # -------------------------
    try:
        init_db()
        logger.info("DB initialized")
    except Exception:
        logger.exception("DB init failed")

    # -------------------------
    # HOME
    # -------------------------
    @app.route("/")
    def index():
        rows = fetch_all_iocs()
        iocs = [dict(r) for r in rows]

        high = sum(1 for x in iocs if x["threat_level"] == "High")
        medium = sum(1 for x in iocs if x["threat_level"] == "Medium")
        low = sum(1 for x in iocs if x["threat_level"] == "Low")

        ip_list = [x["value"] for x in iocs if x["type"] == "ip"]

        return render_template(
            "index.html",
            iocs=iocs,
            count=len(iocs),
            high=high,
            medium=medium,
            low=low,
            ip_list=ip_list
        )

    # -------------------------
    # LOOKUP PAGE
    # -------------------------
    @app.route("/lookup")
    def lookup_page():
        return render_template("lookup.html")

    # -------------------------
    # BACKEND GEO PROXY (🔥 FIX)
    # -------------------------
    @app.route("/api/geo/<ip>")
    def geo_lookup(ip):
        try:
        # -------- FIRST TRY: ip-api (MOST STABLE) --------
            r = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=5
        )
            if r.ok:
                d = r.json()
            if d.get("status") == "success":
                return jsonify({
                    "lat": d.get("lat"),
                    "lon": d.get("lon"),
                    "city": d.get("city"),
                    "country": d.get("country")
                })

        # -------- FALLBACK: ipapi --------
            r = requests.get(
            f"https://ipapi.co/{ip}/json/",
            timeout=5
        )
            if r.ok:
                d = r.json()
            if "latitude" in d and "longitude" in d:
                return jsonify({
                    "lat": d.get("latitude"),
                    "lon": d.get("longitude"),
                    "city": d.get("city"),
                    "country": d.get("country_name")
                })

        # -------- IF BOTH FAIL --------
            return jsonify({"error": "geo lookup failed"}), 200

        except Exception as e:
        # NEVER return 500 to frontend
            return jsonify({"error": str(e)}), 200

    # -------------------------
    # IOC DETAIL
    # -------------------------
    @app.route("/ioc/<int:ioc_id>")
    def ioc_detail(ioc_id):
        rows = fetch_all_iocs()
        ioc = next((dict(r) for r in rows if r["id"] == ioc_id), None)
        if not ioc:
            return "IOC not found", 404

        geo = {}
        try:
            r = requests.get(f"https://ipapi.co/{ioc['value']}/json/", timeout=5)
            if r.ok:
                geo = r.json()
        except Exception:
            pass

        events = [dict(e) for e in fetch_trend_events()]

        return render_template("ioc_detail.html", ioc=ioc, geo=geo, events=events)

    # -------------------------
    # EXPORTS
    # -------------------------
    @app.route("/export/json")
    def export_json():
        return jsonify([dict(r) for r in fetch_all_iocs()])

    @app.route("/export/csv")
    def export_csv():
        rows = fetch_all_iocs()

        def generate():
            header = ["id", "value", "type", "threat_level", "tags", "source", "first_seen", "last_seen"]
            yield ",".join(header) + "\n"
            for r in rows:
                d = dict(r)
                yield ",".join(str(d.get(h, "")) for h in header) + "\n"

        return Response(generate(), mimetype="text/csv",
                        headers={"Content-Disposition": "attachment; filename=iocs.csv"})

    # -------------------------
    # TRENDS API
    # -------------------------
    @app.route("/api/trends")
    def trends():
        events = [dict(e) for e in fetch_trend_events()]
        days = {}
        for e in events:
            day = e["timestamp"].split("T")[0]
            days[day] = days.get(day, 0) + 1

        return jsonify({
            "labels": sorted(days.keys()),
            "values": [days[d] for d in sorted(days.keys())]
        })

    # -------------------------
    # TAG UPDATE
    # -------------------------
    @app.route("/api/tag", methods=["POST"])
    def update_tag():
        data = request.json
        conn = sqlite3.connect("cti.db")
        cur = conn.cursor()
        cur.execute("UPDATE iocs SET tags=? WHERE id=?", (data["tags"], data["id"]))
        conn.commit()
        conn.close()
        return jsonify({"status": "ok"})

    # -------------------------
    # LOOKUP API (FINAL LOGIC)
    # -------------------------
    @app.route("/api/lookup", methods=["POST"])
    def lookup():
        ip = request.json.get("value", "").strip()

        if not ip:
            return jsonify({"error": "No IP provided"}), 400

        vt = vt_lookup_ip(ip)
        abuse = abuse_lookup_ip(ip)

        vt_mal = int(vt.get("malicious", 0))
        vt_susp = int(vt.get("suspicious", 0))
        abuse_score = int(abuse.get("abuse_score", 0))
        abuse_reports = int(abuse.get("total_reports", 0))

        threat_points = 0
        if vt_mal > 0: threat_points += 50
        if vt_susp > 0: threat_points += 20
        if abuse_score >= 75: threat_points += 50
        elif abuse_score >= 50: threat_points += 40
        elif abuse_score >= 25: threat_points += 20
        if abuse_reports >= 10: threat_points += 20

        level = "High" if threat_points >= 70 else "Medium" if threat_points >= 35 else "Low"

        now = datetime.datetime.utcnow().isoformat() + "Z"
        insert_ioc({
            "value": ip,
            "type": "ip",
            "threat_level": level,
            "tags": "",
            "source": "CTI Lookup",
            "first_seen": now,
            "last_seen": now
        })

        return jsonify({
            "status": "ok",
            "threat_level": level,
            "debug": {
                "vt_malicious": vt_mal,
                "vt_suspicious": vt_susp,
                "abuse_score": abuse_score,
                "abuse_reports": abuse_reports,
                "threat_points": threat_points
            },
            "virustotal": vt,
            "abuseipdb": abuse
        })

    # -------------------------
    # HEALTH
    # -------------------------
    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
