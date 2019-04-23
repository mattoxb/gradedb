"""create course table

Revision ID: daa9e8f45e07
Revises: 
Create Date: 2019-04-20 12:17:46.815477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daa9e8f45e07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('courses',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('rubric', sa.String(50), nullable=False),
            sa.Column('semester', sa.String(7), nullable=False),
            sa.Column('title', sa.Unicode(200)),
            sa.UniqueConstraint('rubric','semester'),)

def downgrade():
    op.drop_table('courses')
