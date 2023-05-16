"""add user table

Revision ID: 328d9dc30563
Revises: cb94d37ed3ce
Create Date: 2023-05-16 10:59:05.432106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '328d9dc30563'
down_revision = 'cb94d37ed3ce'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                        server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
