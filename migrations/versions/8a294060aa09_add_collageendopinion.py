"""add CollageEndOpinion

Revision ID: 8a294060aa09
Revises: 43b5f168e3ee
Create Date: 2017-09-07 13:56:34.088004

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8a294060aa09'
down_revision = '43b5f168e3ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('CollageEndOpinion', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'CollageEndOpinion')
    op.create_table('website',
    sa.Column('WebId', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('website', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('remarks', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('WebId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('user_project',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('userid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('pid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pid'], ['project.pid'], name='user_project_ibfk_2'),
    sa.ForeignKeyConstraint(['userid'], ['user.userid'], name='user_project_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('project_mode',
    sa.Column('sid', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('status', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('sid'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('resultstype',
    sa.Column('Rid', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('Rname', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('Rid'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('businessplan',
    sa.Column('BusinessPlanId', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('remarks', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('BusinessPlanId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('User_Project')
    op.drop_table('Website')
    op.drop_table('ResultsType')
    op.drop_table('Project_mode')
    op.drop_table('BusinessPlan')
    # ### end Alembic commands ###
