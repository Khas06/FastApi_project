"""Add users table

Revision ID: 9d31a6a24675
Revises: 0bb500a26eeb
Create Date: 2022-09-07 12:39:36.672623

"""
from venv import create
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d31a6a24675'
down_revision = '0bb500a26eeb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                             sa.Column('email', sa.String(), nullable=False),
                             sa.Column('password', sa.String(), nullable=False),
                             sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                        server_default=sa.text('now()'), nullable=False),
                             sa.PrimaryKeyConstraint('id'),
                             sa.UniqueConstraint('email')
                             )
    pass

def downgrade() -> None:
    op.drop_table('users')
    pass
