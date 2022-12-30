"""add foreign key to posts table

Revision ID: 80137f81b4b3
Revises: 375834f98635
Create Date: 2022-12-30 13:48:42.701206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80137f81b4b3'
down_revision = '375834f98635'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", 
    local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
