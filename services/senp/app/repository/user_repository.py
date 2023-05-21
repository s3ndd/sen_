from app import db_session
from app.model import User


class UserRepository:

    def get_all_users(self):
        return db_session.query(User).all()

    def get_user_by_id(self, user_id: str):
        return db_session.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str) -> User:
        return db_session.query(User).filter(User.username == username).first()

    def get_user_by_email(self, email) -> User:
        return db_session.query(User).filter(User.email == email).first()

    def get_user_by_mobile(self, mobile) -> User:
        return db_session.query(User).filter(User.mobile == mobile).first()

    def create_user(self, user) -> User:
        db_session.add(user)
        db_session.commit()
        return user

    def update_user(self, user) -> User:
        db_session.merge(user)
        db_session.commit()
        return user

    def delete_user_by_id(self, id):
        db_session.query(User).filter(User.id == id).delete()
        db_session.commit()
