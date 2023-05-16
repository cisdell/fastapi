"""create posts table

Revision ID: 48c9c8ea4ad7
Revises:
Create Date: 2023-05-15 16:13:35.676388

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '48c9c8ea4ad7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        )
    pass

def downgrade():
    op.drop_table('posts')
    pass
