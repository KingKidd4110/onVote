"""empty message

Revision ID: 347f4ec5eb5e
Revises: None
Create Date: 2023-3-11 21:47:23.113431

"""

# revision identifiers, used by Alembic.
revision = '347f4ec5eb5e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("polls") as batch_op:
        batch_op.drop_column('status')
    op.add_column('topics', sa.Column('status', sa.Boolean(), default=1))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("topics") as batch_op:
        batch_op.drop_column('status')
    op.add_column('polls', sa.Column('status', sa.BOOLEAN(), nullable=True))
    ### end Alembic commands ###
