import logging
from dataclasses import dataclass
from datetime import datetime
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from api.domain.repositories.user_repository import UserRepository


class UserNotFound(Exception):
    pass


class UserCredentialsInvalid(Exception):
    pass


@dataclass
class User:
    username: str
    role: str
    password: str
    update_at: datetime
    insert_at: datetime

    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def authenticate(cls, username: str, password: str, repository: UserRepository):
        user = repository.get_user(username)
        if not user:
            raise UserNotFound("User not found")

        if cls.check_password(user.password, password):
            token = create_access_token(identity={"username": username, "role": user.role})
            return token
        else:
            raise UserCredentialsInvalid("User credentials invalid")
