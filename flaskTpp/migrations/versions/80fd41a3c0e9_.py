"""empty message

Revision ID: 80fd41a3c0e9
Revises: 39bf10eec295
Create Date: 2020-03-21 14:34:15.430456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80fd41a3c0e9'
down_revision = '39bf10eec295'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('letter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('letter', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('letter_id', sa.Integer(), nullable=True),
    sa.Column('c_id', sa.Integer(), nullable=True),
    sa.Column('c_parent_id', sa.Integer(), nullable=True),
    sa.Column('c_region_name', sa.String(length=16), nullable=True),
    sa.Column('c_city_code', sa.Integer(), nullable=True),
    sa.Column('c_pinyin', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['letter_id'], ['letter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    op.drop_table('letter')
    # ### end Alembic commands ###