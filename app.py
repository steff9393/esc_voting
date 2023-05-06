import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from flask import Flask
from routes import *

DB_URL = os.getenv("DB_URL")


app = Flask(__name__, template_folder="templates")

# Setting up DB connection
engine = create_engine(DB_URL)
Base = declarative_base()

# Start session
SessionLocal = sessionmaker(bind=engine)


# Definition of starting
if __name__ == "__main__":
    app.run()
