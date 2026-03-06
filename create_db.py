import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

try:
    db_url = os.getenv("DATABASE_URL")
    parsed_url = urlparse(db_url)
    
    # Connect to the default 'postgres' database to create the new target DB
    conn = psycopg2.connect(
        dbname="postgres",
        user=parsed_url.username or "postgres",
        password=parsed_url.password or "admin",
        host=parsed_url.hostname or "localhost",
        port=parsed_url.port or "5432",
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    # The target database we want to create
    target_db = parsed_url.path.lstrip('/')
    
    # We cannot bind parameters safely to CREATE DATABASE in psycopg2, so string format is used carefully
    cursor.execute(f"CREATE DATABASE {target_db}")
    cursor.close()
    conn.close()
    print(f"Database {target_db} created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print("Database property_db already exists.")
except Exception as e:
    print(f"Error creating database: {e}")
