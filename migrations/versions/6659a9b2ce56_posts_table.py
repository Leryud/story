"""posts table

Revision ID: 6659a9b2ce56
Revises: 47f4eb7cf37d
Create Date: 2021-06-13 19:29:51.176500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6659a9b2ce56'
down_revision = '47f4eb7cf37d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('story',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_story_timestamp'), 'story', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_story_timestamp'), table_name='story')
    op.drop_table('story')
    # ### end Alembic commands ###
