"""Add foreign-key to posts table

Revision ID: 5550e3bafc91
Revises: 9d31a6a24675
Create Date: 2022-09-07 13:46:29.283565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5550e3bafc91'
down_revision = '9d31a6a24675'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table="users",
                           local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')

    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass