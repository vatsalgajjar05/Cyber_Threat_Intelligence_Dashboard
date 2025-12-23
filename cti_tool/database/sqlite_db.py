import sqlite3
import os

# ==========================================================
#  DATABASE PATH (CENTRALIZED)
# ==========================================================
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "cti.db")

# Ensure database folder exists
os.makedirs(DB_DIR, exist_ok=True)


# ==========================================================
#  DB CONNECTION
# ==========================================================
def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================================================
#  INITIALIZE DATABASE
# ==========================================================
def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # ===========================
    # IOC TABLE
    # ===========================
    cur.execute("""
        CREATE TABLE IF NOT EXISTS iocs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value TEXT NOT NULL,
            type TEXT NOT NULL,
            threat_level TEXT,
            tags TEXT,
            source TEXT,
            first_seen TEXT,
            last_seen TEXT
        )
    """)

    # ===========================
    # EVENTS TABLE
    # ===========================
    cur.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ioc_value TEXT NOT NULL,
            event_type TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ==========================================================
#  INSERT IOC + EVENT
# ==========================================================
def insert_ioc(ioc):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO iocs (
            value, type, threat_level,
            tags, source, first_seen, last_seen
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        ioc["value"],
        ioc["type"],
        ioc.get("threat_level", "unknown"),
        ioc.get("tags", ""),
        ioc.get("source", "unknown"),
        ioc.get("first_seen"),
        ioc.get("last_seen"),
    ))

    # Insert trend event
    cur.execute("""
        INSERT INTO events (ioc_value, event_type, timestamp)
        VALUES (?, ?, ?)
    """, (
        ioc["value"],
        "lookup",
        ioc["first_seen"]
    ))

    conn.commit()
    conn.close()


# ==========================================================
#  FETCH ALL IOCs
# ==========================================================
def fetch_all_iocs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM iocs ORDER BY id DESC")
    rows = cur.fetchall()

    conn.close()
    return rows


# ==========================================================
#  FIND IOC BY VALUE
# ==========================================================
def find_ioc(value):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM iocs WHERE value = ?", (value,))
    row = cur.fetchone()

    conn.close()
    return row


# ==========================================================
#  FETCH EVENTS (FOR TRENDS)
# ==========================================================
def fetch_trend_events():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM events ORDER BY timestamp ASC")
    rows = cur.fetchall()

    conn.close()
    return rows
