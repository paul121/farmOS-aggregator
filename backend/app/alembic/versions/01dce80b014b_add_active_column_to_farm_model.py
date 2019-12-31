"""Add active column to Farm model

Revision ID: 01dce80b014b
Revises: c717af8cff85
Create Date: 2019-12-31 16:17:38.710645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01dce80b014b'
down_revision = 'c717af8cff85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('farm', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('farm', 'active')
    # ### end Alembic commands ###