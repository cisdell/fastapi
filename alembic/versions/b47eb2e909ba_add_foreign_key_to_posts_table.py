"""add foreign-key to posts table

Revision ID: b47eb2e909ba
Revises: 328d9dc30563
Create Date: 2023-05-16 11:37:59.098332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b47eb2e909ba'
down_revision = '328d9dc30563'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
