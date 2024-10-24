from sqlalchemy import Column, Integer, String
from models.base import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    points = Column(Integer, nullable=False)

    @staticmethod
    def get_all(session):
        return session.query(Activity).all()
