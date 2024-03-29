"""empty message

Revision ID: d9320aa6ee51
Revises: 
Create Date: 2023-07-26 12:06:57.991136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9320aa6ee51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('house', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('good', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wood_type', sa.String(length=64), nullable=True),
    sa.Column('core_type', sa.String(length=64), nullable=True),
    sa.Column('plyable', sa.Boolean(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wands')
    op.drop_table('students')
    # ### end Alembic commands ###
