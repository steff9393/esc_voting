import os
from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
# import psycopg2

# Set Env variables
DB_URL = os.getenv("DB_URL")
PASSWD = os.getenv("PASSWD")

app = Flask(__name__, template_folder="templates")

# Set up database connection
engine = create_engine(DB_URL)
Base = declarative_base()


# Database Table definition
class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    country1 = Column(Text)
    comment1 = Column(Text)
    country2 = Column(Text)
    comment2 = Column(Text)
    country3 = Column(Text)
    comment3 = Column(Text)
    country4 = Column(Text)
    comment4 = Column(Text)

    def __repr__(self):
        return f"<Vote(name='{self.name}', country1={self.country1}, country2={self.country2}, country3={self.country3}, country4={self.country4})>"


# Start session
SessionLocal = sessionmaker(bind=engine)


# Main route. Welcome Screen with formular
@app.route("/")
def run():
    return render_template("index.html")


# Post Methode write votings to PostgreSQL DB
@app.route("/vote", methods=["POST"])
def save_vote():
    password = request.form.get("password")
    if password != PASSWD:
        return "Invalid password"

    name = request.form.get("name")
    country1 = int(request.form.get("country1"))
    comment1 = request.form.get("comment1")
    country2 = int(request.form.get("country2"))
    comment2 = request.form.get("comment2")
    country3 = int(request.form.get("country3"))
    comment3 = request.form.get("comment3")
    country4 = int(request.form.get("country4"))
    comment4 = request.form.get("comment4")

    # Create a new Vote object with the submitted data
    new_vote = Vote(
        name=name,
        country1=country1,
        comment1=comment1,
        country2=country2,
        comment2=comment2,
        country3=country3,
        comment3=comment3,
        country4=country4,
        comment4=comment4,
    )

    # Add the new Vote object to the database
    session = SessionLocal()
    session.add(new_vote)
    session.commit()

    return f"Danke, {name}. Deine Bewertung wurde übermittelt! Deine ID ist: {new_vote.id}. Bitte aufschreiben."


# Hidden delete functionality
@app.route("/delete/<int:id>", methods=["GET"])
def del_vote(id: int):
    session = SessionLocal()
    obj = session.query(Vote).filter(Vote.id == id).first()
    session.delete(obj)
    session.commit()
    return f"{id} ist gelöscht"


@app.route('/update/<int:id>', methods=['GET', 'PUT', 'POST'])
def update_vote(id: int):
    new_country1 = request.args.get('country1')
    new_country2 = request.args.get('country2')
    new_country3 = request.args.get('country3')
    new_country4 = request.args.get('country4')

    session = SessionLocal()
    obj = session.query(Vote).filter(Vote.id == id).first()

    if obj:
        for i, new_country in enumerate([new_country1, new_country2, new_country3, new_country4], 1):
            if new_country is not None:
                setattr(obj, f'country{i}', new_country)

    else:
        return f"ID:{id} nicht gefunden"

    session.commit()
    session.close()

    return f"Update erfolgreich für {id}"


# Definition of starting
if __name__ == "__main__":
    app.run()
