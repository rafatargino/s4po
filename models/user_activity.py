from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base

class UserActivity(Base):
    __tablename__ = "user_activities"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    status = Column(String, nullable=False)
    justification = Column(String, nullable=True)

    user = relationship("User")
    activity = relationship("Activity")

    @staticmethod
    def save(session, user_activity):
        session.add(user_activity)
        session.commit()

    @staticmethod
    def get_user_id_by_name(session, name):
        user = session.query(User).filter_by(name=name).first()
        return user.id if user else None
