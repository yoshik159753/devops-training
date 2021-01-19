"""create users table

Revision ID: da5c307739c6
Revises:
Create Date: 2021-01-16 22:02:55.313782

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'da5c307739c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.dialects.postgresql.UUID, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )


def downgrade():
    op.drop_table('users')
