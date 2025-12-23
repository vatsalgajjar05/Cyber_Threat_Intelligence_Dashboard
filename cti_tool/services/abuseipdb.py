import requests
from config import Config

API_URL = "https://api.abuseipdb.com/api/v2/check"


def abuse_lookup_ip(ip):
    """
    Lookup IP reputation from AbuseIPDB (Free Tier Compatible)

    Returns:
        abuse_score      -> Abuse confidence score (0–100)
        total_reports    -> Number of reports
        last_reported    -> Last reported timestamp (if available)
    """

    headers = {
        "Key": Config.ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,      # wider window = better detection
        "verbose": True
    }

    try:
        r = requests.get(API_URL, headers=headers, params=params, timeout=10)
    except Exception as e:
        return {
            "error": True,
            "reason": f"AbuseIPDB request failed: {e}"
        }

    if r.status_code != 200:
        return {
            "error": True,
            "reason": f"AbuseIPDB HTTP {r.status_code}"
        }

    data = r.json().get("data", {})

    return {
        "source": "AbuseIPDB",
        "abuse_score": data.get("abuseConfidenceScore", 0),
        "total_reports": data.get("totalReports", 0),
        "last_reported": data.get("lastReportedAt"),
        "country": data.get("countryCode", "Unknown"),
        "isp": data.get("isp", "Unknown"),
        "domain": data.get("domain", "Unknown"),
        "usage_type": data.get("usageType", "Unknown"),
        "link": f"https://www.abuseipdb.com/check/{ip}",
        "error": False
    }
