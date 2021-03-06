"""empty message

Revision ID: 5310eac4c002
Revises: e7526d381686
Create Date: 2021-05-08 16:34:19.814137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5310eac4c002'
down_revision = 'e7526d381686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###
