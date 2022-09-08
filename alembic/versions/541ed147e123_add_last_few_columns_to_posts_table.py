"""Add last few columns to posts table

Revision ID: 541ed147e123
Revises: 5550e3bafc91
Create Date: 2022-09-08 19:22:44.239489

"""
from venv import create
from wsgiref.simple_server import server_version
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '541ed147e123'
down_revision = '5550e3bafc91'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.String, nullable=False, server_default=sa.text('TRUE')))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                  nullable=False, server_default=sa.text("now()")))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
