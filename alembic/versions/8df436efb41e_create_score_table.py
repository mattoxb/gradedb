"""Create Score Table

Revision ID: 8df436efb41e
Revises: 5a830f6f2208
Create Date: 2019-04-22 07:46:32.997204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8df436efb41e'
down_revision = '5a830f6f2208'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('scores',
                    sa.Column('id',sa.Integer, primary_key=True),
                    sa.Column('assignment_id',sa.Integer, sa.ForeignKey('assignments.id'), nullable=False),
                    sa.Column('student_id',sa.Integer, sa.ForeignKey('students.id'), nullable=False),
                    sa.Column('status',sa.String(1),nullable=False) ,
                    sa.Column('raw',sa.Float),
                    sa.Column('factor',sa.Float),
                    sa.Column('norm',sa.Float),
                    sa.Column('points',sa.Float),
                    sa.UniqueConstraint('assignment_id','student_id'))

def downgrade():
    op.drop_table('scores')
