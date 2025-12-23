import os
from dotenv import load_dotenv

load_dotenv()  # reads .env in project root

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret")
    ENV = os.getenv("FLASK_ENV", "production")
    DEBUG = ENV == "development"

    # APIs
    VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "")
    ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY", "")
    

