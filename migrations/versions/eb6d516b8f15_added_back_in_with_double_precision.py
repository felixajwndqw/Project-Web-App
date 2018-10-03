"""Added back in with DOUBLE_PRECISION

Revision ID: eb6d516b8f15
Revises: e82e18e751e9
Create Date: 2018-10-03 11:36:15.410946

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eb6d516b8f15'
down_revision = 'e82e18e751e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('galaxy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dec', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('ra', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.create_index(batch_op.f('ix_galaxy_dec'), ['dec'], unique=False)
        batch_op.create_index(batch_op.f('ix_galaxy_ra'), ['ra'], unique=False)

    with op.batch_alter_table('shape', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dec1', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('dec2', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('dec3', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('dec_points', postgresql.ARRAY(postgresql.DOUBLE_PRECISION(precision=15)), nullable=True))
        batch_op.add_column(sa.Column('dec_wh', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('dec_xy', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('r', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('ra1', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('ra2', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('ra3', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('ra_points', postgresql.ARRAY(postgresql.DOUBLE_PRECISION(precision=15)), nullable=True))
        batch_op.add_column(sa.Column('ra_wh', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('ra_xy', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('theta', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('x0', postgresql.DOUBLE_PRECISION(precision=15), nullable=False))
        batch_op.add_column(sa.Column('x1', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('x2', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('x3', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('x_points', postgresql.ARRAY(postgresql.DOUBLE_PRECISION(precision=15)), nullable=True))
        batch_op.add_column(sa.Column('xw', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('y0', postgresql.DOUBLE_PRECISION(precision=15), nullable=False))
        batch_op.add_column(sa.Column('y1', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('y2', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('y3', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))
        batch_op.add_column(sa.Column('y_points', postgresql.ARRAY(postgresql.DOUBLE_PRECISION(precision=15)), nullable=True))
        batch_op.add_column(sa.Column('yh', postgresql.DOUBLE_PRECISION(precision=15), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shape', schema=None) as batch_op:
        batch_op.drop_column('yh')
        batch_op.drop_column('y_points')
        batch_op.drop_column('y3')
        batch_op.drop_column('y2')
        batch_op.drop_column('y1')
        batch_op.drop_column('y0')
        batch_op.drop_column('xw')
        batch_op.drop_column('x_points')
        batch_op.drop_column('x3')
        batch_op.drop_column('x2')
        batch_op.drop_column('x1')
        batch_op.drop_column('x0')
        batch_op.drop_column('theta')
        batch_op.drop_column('ra_xy')
        batch_op.drop_column('ra_wh')
        batch_op.drop_column('ra_points')
        batch_op.drop_column('ra3')
        batch_op.drop_column('ra2')
        batch_op.drop_column('ra1')
        batch_op.drop_column('r')
        batch_op.drop_column('dec_xy')
        batch_op.drop_column('dec_wh')
        batch_op.drop_column('dec_points')
        batch_op.drop_column('dec3')
        batch_op.drop_column('dec2')
        batch_op.drop_column('dec1')

    with op.batch_alter_table('galaxy', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_galaxy_ra'))
        batch_op.drop_index(batch_op.f('ix_galaxy_dec'))
        batch_op.drop_column('ra')
        batch_op.drop_column('dec')

    # ### end Alembic commands ###
