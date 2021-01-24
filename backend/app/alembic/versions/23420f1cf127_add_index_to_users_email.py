"""add index to users email

Revision ID: 23420f1cf127
Revises: da5c307739c6
Create Date: 2021-01-23 16:30:22.179930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23420f1cf127'
down_revision = 'da5c307739c6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('ik_users_email', 'users', ['email'], unique=True)


def downgrade():
    op.drop_index('ik_users_email')
