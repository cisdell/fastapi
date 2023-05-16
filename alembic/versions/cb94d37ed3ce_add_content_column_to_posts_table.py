"""add content column to posts table

Revision ID: cb94d37ed3ce
Revises: 48c9c8ea4ad7
Create Date: 2023-05-16 10:48:21.973190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb94d37ed3ce'
down_revision = '48c9c8ea4ad7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        )
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
