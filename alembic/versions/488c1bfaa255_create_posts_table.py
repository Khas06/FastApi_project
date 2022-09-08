"""create posts table

Revision ID: 488c1bfaa255
Revises: 
Create Date: 2022-09-07 12:22:46.277283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '488c1bfaa255'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                             sa.Column('title', sa.String, nullable=False))
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
