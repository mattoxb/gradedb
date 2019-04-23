"""Create Assignment Table

Revision ID: 5a830f6f2208
Revises: 49174de9c93a
Create Date: 2019-04-22 06:30:33.361754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a830f6f2208'
down_revision = '49174de9c93a'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('assignments',
                  sa.Column('id', sa.Integer, primary_key=True),
                  sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id')),
                  sa.Column('parent_id', sa.Integer, sa.ForeignKey('assignments.id')),

                  sa.Column('slug',sa.String,nullable=False) ,
                  sa.Column('title',sa.String,nullable=False),
                  sa.Column('max',sa.Integer),
                  sa.Column('factor',sa.Float),
                  sa.Column('weight',sa.Integer),
                  sa.Column('order',sa.Integer),
                  sa.Column('extra',sa.Integer),
                  sa.UniqueConstraint('course_id','slug'))


def downgrade():
    op.drop_table('assignments')
