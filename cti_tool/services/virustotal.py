import requests
from config import Config

VT_URL = "https://www.virustotal.com/api/v3/ip_addresses/"


def vt_lookup_ip(ip):
    """
    Lookup IP reputation from VirusTotal (Free Tier Compatible)

    Returns:
        malicious   -> number of engines marking IP malicious
        suspicious  -> number of engines marking IP suspicious
    """

    headers = {
        "x-apikey": Config.VT_API_KEY
    }

    try:
        r = requests.get(VT_URL + ip, headers=headers, timeout=10)
    except Exception as e:
        return {
            "error": True,
            "reason": f"VirusTotal request failed: {e}"
        }

    if r.status_code != 200:
        return {
            "error": True,
            "reason": f"VirusTotal HTTP {r.status_code}"
        }

    data = r.json()

    attributes = data.get("data", {}).get("attributes", {})
    stats = attributes.get("last_analysis_stats", {})

    malicious = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)
    harmless = stats.get("harmless", 0)
    undetected = stats.get("undetected", 0)

    return {
        "source": "VirusTotal",
        "malicious": malicious,
        "suspicious": suspicious,
        "harmless": harmless,
        "undetected": undetected,
        # IMPORTANT: do NOT rely only on score for free tier
        "score": malicious + suspicious,
        "country": attributes.get("country", "Unknown"),
        "as_owner": attributes.get("as_owner", "Unknown"),
        "link": f"https://www.virustotal.com/gui/ip-address/{ip}",
        "error": False
    }
