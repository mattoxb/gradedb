"""Create Student Table

Revision ID: 49174de9c93a
Revises: daa9e8f45e07
Create Date: 2019-04-21 15:22:53.072772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49174de9c93a'
down_revision = 'daa9e8f45e07'
branch_labels = None
depends_on = None


def upgrade():

  op.create_table('students',
                  sa.Column('id', sa.Integer, primary_key=True),
                  sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id')),
                  sa.Column('netid', sa.String(9), nullable=False),
                  sa.Column('status', sa.String(1), nullable=False),
                  sa.Column('uin', sa.String(9)),
                  sa.Column('gender',sa.String(3)),
                  sa.Column('lname',sa.String),
                  sa.Column('fname',sa.String),
                  sa.Column('credit',sa.Integer),
                  sa.Column('level',sa.String(2)),
                  sa.Column('year',sa.String),
                  sa.Column('subject',sa.String),
                  sa.Column('number',sa.String(4)),
                  sa.Column('section',sa.String(4)),
                  sa.Column('crn',sa.Integer),
                  sa.Column('degree',sa.String),
                  sa.Column('major',sa.String),
                  sa.Column('college',sa.String),
                  sa.Column('program_code',sa.String),
                  sa.Column('program_name',sa.String),
                  sa.Column('ferpa',sa.String(1)),
                  sa.Column('comments',sa.Integer),
                  sa.Column('pname',sa.String),
                  sa.Column('admit_term',sa.String),
                  sa.Column('email',sa.String),
                  sa.UniqueConstraint('course_id','netid'),)

def downgrade():
    op.drop_table('students')
