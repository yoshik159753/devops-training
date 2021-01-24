"""add password digest to users

Revision ID: f3f6864b8124
Revises: 23420f1cf127
Create Date: 2021-01-24 21:39:00.882133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3f6864b8124'
down_revision = '23420f1cf127'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('password_digest', sa.String(255)))


def downgrade():
    op.drop_column('users', 'password_digest')
