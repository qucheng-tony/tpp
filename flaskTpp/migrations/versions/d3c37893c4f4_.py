"""empty message

Revision ID: d3c37893c4f4
Revises: 1f08cdcf3441
Create Date: 2020-03-22 22:04:45.701896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3c37893c4f4'
down_revision = '1f08cdcf3441'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_movies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_cinema_id', sa.Integer(), nullable=True),
    sa.Column('c_movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_cinema_id'], ['cinema_user.id'], ),
    sa.ForeignKeyConstraint(['c_movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinema_movies')
    # ### end Alembic commands ###
