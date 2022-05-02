"""add mi table

Revision ID: 2c884219fd26
Revises: 4aa9e6e6f5e5
Create Date: 2022-02-06 10:29:52.284975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c884219fd26'
down_revision = '4aa9e6e6f5e5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'radon_mi_metric',
        sa.Column('name', sa.VARCHAR),
        sa.Column('module_name', sa.VARCHAR),
        sa.Column('mi', sa.NUMERIC)
    )

def downgrade():
    op.drop_table('radon_mi_metric')
