import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    # Connect to the default 'postgres' database
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE property_db")
    cursor.close()
    conn.close()
    print("Database property_db created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print("Database property_db already exists.")
except Exception as e:
    print(f"Error creating database: {e}")
