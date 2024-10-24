from models.activity import Activity
from models.base import SessionLocal

class ActivityController:
    @staticmethod
    def list_activities():
        session = SessionLocal()
        try:
            return Activity.get_all(session)
        finally:
            session.close()
