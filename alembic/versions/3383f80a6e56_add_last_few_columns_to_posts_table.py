"""add last few columns to posts table

Revision ID: 3383f80a6e56
Revises: b47eb2e909ba
Create Date: 2023-05-16 13:10:51.477813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3383f80a6e56'
down_revision = 'b47eb2e909ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
