import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    conn = psycopg2.connect(
        dbname="property_db",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
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
