"""empty message

Revision ID: 77490bb2e9d8
Revises: 35f8893ffa7c
Create Date: 2020-03-22 15:26:59.060000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77490bb2e9d8'
down_revision = '35f8893ffa7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('movie_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('p_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('p_name')
    )
    op.create_table('cinema_user_permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_user_id', sa.Integer(), nullable=True),
    sa.Column('c_perssion_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_perssion_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['c_user_id'], ['cinema_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('name', table_name='user')
    op.drop_index('phone', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('_password', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('is_delete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('permission', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('phone', 'user', ['phone'], unique=True)
    op.create_index('name', 'user', ['name'], unique=True)
    op.drop_table('cinema_user_permission')
    op.drop_table('permissions')
    op.drop_table('movie_user')
    op.drop_table('cinema_user')
    # ### end Alembic commands ###