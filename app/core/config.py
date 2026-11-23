import os
import dotenv

dotenv.load_dotenv()

APP_NAME = os.getenv("APP_NAME","DocuVault")
DEBUG = os.getenv("DEBUG","False").lower() == "True"

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT","5432"))
DB_NAME = os.getenv("DB_NAME", "DocuVault")

if not DB_PASSWORD:
    raise ValueError("DB_PASSWORD is missing from .env")
