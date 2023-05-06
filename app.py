from .routes import *
from .database import Base, SessionLocal
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from flask import Flask

app = Flask(__name__, template_folder="templates")


# Definition of starting
if __name__ == "__main__":
    app.run()
