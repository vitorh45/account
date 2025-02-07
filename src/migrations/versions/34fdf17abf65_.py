"""empty message

Revision ID: 34fdf17abf65
Revises: 
Create Date: 2024-10-08 15:21:07.665569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34fdf17abf65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('insert_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('username', name=op.f('user_pkey')),
    sa.UniqueConstraint('username', name=op.f('user_username_key'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
