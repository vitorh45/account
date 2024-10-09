from datetime import datetime

from api.app import db
from sqlalchemy import Table, Column, String
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "user"

    username = Column(db.String(150), nullable=False, primary_key=True)
    role = Column(db.String(20), nullable=False)
    password = Column(db.String(250), nullable=False)
    insert_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_at = Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
