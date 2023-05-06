import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
