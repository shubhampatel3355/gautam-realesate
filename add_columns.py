import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

try:
    # the environment variable is a full dsn url string
    db_url = os.getenv("DATABASE_URL")
    conn = psycopg2.connect(db_url)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(
        "ALTER TABLE properties ADD COLUMN IF NOT EXISTS property_for VARCHAR;"
    )
    cursor.execute("ALTER TABLE properties ADD COLUMN IF NOT EXISTS sqft VARCHAR;")
    cursor.close()
    conn.close()
    print("Database columns 'property_for' and 'sqft' added successfully.")
except Exception as e:
    print(f"Error updating database: {e}")
