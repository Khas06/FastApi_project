"""add column content to table posts

Revision ID: 0bb500a26eeb
Revises: 488c1bfaa255
Create Date: 2022-09-07 12:23:03.548610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bb500a26eeb'
down_revision = '488c1bfaa255'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
