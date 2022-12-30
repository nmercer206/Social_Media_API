"""add content column to posts table

Revision ID: 6476157767c3
Revises: cef2fa40322e
Create Date: 2022-12-30 13:12:17.512255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6476157767c3'
down_revision = 'cef2fa40322e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
