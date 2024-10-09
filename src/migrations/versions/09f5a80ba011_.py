"""empty message

Revision ID: 09f5a80ba011
Revises: 34fdf17abf65
Create Date: 2024-10-08 17:55:04.799751

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from werkzeug.security import generate_password_hash


# revision identifiers, used by Alembic.
revision = '09f5a80ba011'
down_revision = '34fdf17abf65'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        sa.table('user',
                 sa.column('username'),
                 sa.column('role'),
                 sa.column('password'),
                 sa.column('update_at'),
                 sa.column('insert_at')),
        [
            {
                "username": "user",
                "role": "user",
                "password": generate_password_hash("L0XuwPOdS5U"),
                'update_at': datetime.utcnow(),
                'insert_at': datetime.utcnow()
            },
            {
                "username": "admin",
                "role": "admin",
                "password": generate_password_hash("JKSipm0YH"),
                'update_at': datetime.utcnow(),
                'insert_at': datetime.utcnow()
            }
        ]
    )


def downgrade():
    pass
