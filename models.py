from .app import Base
from sqlalchemy import Column, Integer, String, Text
from .database import Base, SessionLocal


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