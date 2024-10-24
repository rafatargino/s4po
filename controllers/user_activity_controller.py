from models.user_activity import UserActivity
from models.base import SessionLocal

class UserActivityController:
    @staticmethod
    def register_activity(user_name, activity_id, status, justification):
        session = SessionLocal()
        try:
            user_id = UserActivity.get_user_id_by_name(session, user_name)
            if user_id is None:
                raise ValueError(f"Usuário {user_name} não encontrado.")

            user_activity = UserActivity(
                user_id=user_id,
                activity_id=activity_id,
                status=status,
                justification=justification
            )
            UserActivity.save(session, user_activity)
        finally:
            session.close()
