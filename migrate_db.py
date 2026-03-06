import sys
import os

# Ensure we can import from the backend directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, text
from database import SQLALCHEMY_DATABASE_URL

print("Connecting to database...")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

with engine.connect() as conn:
    print("Executing ALTER TABLE...")
    conn.execute(text("ALTER TABLE properties ADD COLUMN dynamic_fields JSON;"))
    conn.commit()
    print("Migration successful.")
