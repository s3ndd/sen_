from typing import List

from app.model import User
from app.repository import UserRepository
from app.schema import UserSchema


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()
        self.user_schema = UserSchema()

    def get_all_users(self) -> List[UserSchema]:
        users = self.user_repository.get_all_users()
        return self.user_schema.dump(users, many=True)

    def get_user_by_id(self, user_id: str) -> UserSchema:
        user = self.user_repository.get_user_by_id(user_id)
        return None if user is None else self.user_schema.dump(user)

    def get_user_by_username(self, username: str) -> UserSchema:
        user = self.user_repository.get_user_by_username(username)
        return None if user is None else self.user_schema.dump(user)

    def get_user_by_email(self, email: str) -> UserSchema:
        user = self.user_repository.get_user_by_email(email)
        return None if user is None else self.user_schema.dump(user)

    def get_user_by_mobile(self, mobile: str) -> UserSchema:
        user = self.user_repository.get_user_by_mobile(mobile)
        return None if user is None else self.user_schema.dump(user)

    def create_user(self, data: dict) -> UserSchema:
        user_data = self.user_schema.load(data)
        user = User(**user_data)
        return self.user_schema.dump(self.user_repository.create_user(user))

    def update_user(self, user_id: str, data: dict) -> UserSchema:
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user_data = self.user_schema.load(data, partial=True)
            for key, value in user_data.items():
                setattr(user, key, value)
            return self.user_schema.dump(self.user_repository.update_user(user))

        return None

    def delete_user_by_id(self, user_id: str) -> bool:
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            self.user_repository.delete_user_by_id(user_id)
            return True
        return False
