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

from flask import Flask, jsonify, render_template, request, redirect, session
from auth import login_required
import sqlite3
import os

# ---------------- CONFIG (ADMIN ONLY) ----------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
SECRET_KEY = "admin_panel_secret"

# Path to main CTI database (shared)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "database", "cti.db")


# ---------------- APP ----------------
app = Flask(__name__, template_folder="templates")
app.secret_key = SECRET_KEY


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- LOGIN ----------------
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if (
            request.form.get("username") == ADMIN_USERNAME and
            request.form.get("password") == ADMIN_PASSWORD
        ):
            session["admin_logged_in"] = True
            return redirect("/admin")

        return render_template("admin_login.html", error="Invalid credentials")

    return render_template("admin_login.html")


# ---------------- LOGOUT ----------------
@app.route("/admin/logout")
@login_required
def admin_logout():
    session.clear()
    return redirect("/admin/login")


# ---------------- DASHBOARD ----------------
@app.route("/admin")
@login_required
def admin_dashboard():
    conn = get_db()
    rows = conn.execute("SELECT * FROM iocs").fetchall()
    conn.close()

    return render_template(
        "admin_dashboard.html",
        total=len(rows),
        high=sum(1 for r in rows if r["threat_level"] == "High"),
        medium=sum(1 for r in rows if r["threat_level"] == "Medium"),
        low=sum(1 for r in rows if r["threat_level"] == "Low"),
    )


# ---------------- IOC LIST ----------------
@app.route("/admin/iocs")
@login_required
def admin_iocs():
    conn = get_db()
    rows = conn.execute("SELECT * FROM iocs ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("admin_ioc_list.html", iocs=rows)


# ---------------- EDIT IOC ----------------
@app.route("/admin/ioc/<int:ioc_id>", methods=["GET", "POST"])
@login_required
def admin_edit_ioc(ioc_id):
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        cur.execute(
            "UPDATE iocs SET threat_level=?, tags=? WHERE id=?",
            (request.form["threat_level"], request.form["tags"], ioc_id)
        )
        conn.commit()
        conn.close()
        return redirect("/admin/iocs")

    ioc = cur.execute("SELECT * FROM iocs WHERE id=?", (ioc_id,)).fetchone()
    conn.close()

    if not ioc:
        return "IOC not found", 404

    return render_template("admin_edit_ioc.html", ioc=ioc)


# ---------------- DELETE IOC ----------------
# ---------------- DELETE IOC (FIXED) ----------------
@app.route("/admin/api/delete/<int:ioc_id>", methods=["DELETE"])
@login_required
def delete_ioc(ioc_id):
    try:
        conn = sqlite3.connect(DB_PATH)   # ✅ CORRECT DB
        cur = conn.cursor()

        cur.execute("DELETE FROM iocs WHERE id = ?", (ioc_id,))

        if cur.rowcount == 0:
            conn.close()
            return jsonify({"status": "error", "message": "IOC not found"}), 404

        conn.commit()
        conn.close()

        return jsonify({"status": "ok"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(port=8080, debug=True)
