from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection string: username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/property_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
