"""users table

Revision ID: 5f50b2014e5d
Revises: e993c064eade
Create Date: 2021-06-13 22:34:48.176460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f50b2014e5d'
down_revision = 'e993c064eade'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profilePicture', sa.String(length=1024), nullable=True))
    op.drop_column('user', 'profilePicture_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profilePicture_path', sa.VARCHAR(length=1024), nullable=True))
    op.drop_column('user', 'profilePicture')
    # ### end Alembic commands ###
