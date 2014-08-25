"""empty message

Revision ID: ac34d8c1fa0
Revises: 7041a268ec2
Create Date: 2014-08-18 19:53:44.452241

"""

# revision identifiers, used by Alembic.
revision = 'ac34d8c1fa0'
down_revision = '7041a268ec2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_image', sa.String(length=100), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profile_image')
    ### end Alembic commands ###