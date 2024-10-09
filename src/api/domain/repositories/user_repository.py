from abc import ABC
import logging
from typing import Union, Optional
from uuid import UUID

from api.app import db
from api.infrastructure.database.models import User as UserTable


logger = logging.getLogger("accounttest")


class UserRepository(ABC):
    @classmethod
    def get_user(cls, username: str, password: str) -> "User":
        raise NotImplementedError


class SQLAlchemyUserRepository(UserRepository):
    @staticmethod
    def _build_user(user) -> "User":
        from api.domain.entities.user import User
        return User(
            username=user.username,
            password=user.password,
            role=user.role,
            insert_at=user.insert_at,
            update_at=user.update_at,
        )

    @classmethod
    def get_user(
        cls,
        username: str
    ) -> "User":
        logger.info(
            "Getting the user.",
            extra={
                "props": {
                    "service": "PostgreSQL",
                    "service_method": "get_user",
                    "username": username
                }
            },
        )
        try:
            user = UserTable.query.filter_by(username=username).first()
        except Exception as e:
            db.session.rollback()
            logger.exception(
                "Error while trying to get the user",
                extra={
                    "props": {
                        "service": "PostgreSQL",
                        "service_method": "get_user",
                        "username": username
                    }
                },
            )
            raise e

        if not user:
            return None

        return cls._build_user(user=user)
