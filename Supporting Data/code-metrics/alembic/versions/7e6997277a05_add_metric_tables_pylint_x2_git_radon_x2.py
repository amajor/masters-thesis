"""add metric tables, pylint x2, git, radon x2

Revision ID: 7e6997277a05
Revises: 
Create Date: 2019-02-21 20:47:45.774259

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7e6997277a05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pylint_metrics',
        sa.Column('name', sa.VARCHAR),
        sa.Column('module_name', sa.VARCHAR),
        sa.Column('n_refactor', sa.Integer),
        sa.Column('n_convention', sa.Integer),
        sa.Column('statement', sa.Integer),
        sa.Column('global_note', sa.Numeric)
    )

    op.create_table(
        'pylint_metrics_by_msg',
        sa.Column('name', sa.VARCHAR),
        sa.Column('module_name', sa.VARCHAR),
        sa.Column('msg', sa.VARCHAR),
        sa.Column('code', sa.VARCHAR),
        sa.Column('n', sa.Integer)
    )

    op.create_table(
        'git_metrics',
        sa.Column('name', sa.VARCHAR),
        sa.Column('module_name', sa.VARCHAR),
        sa.Column('commit_digest', sa.VARCHAR),
        sa.Column('author', sa.VARCHAR),
        sa.Column('commited_at', sa.VARCHAR),
        sa.Column('commit_msg', sa.VARCHAR),
        sa.Column('lines_added', sa.Integer),
        sa.Column('lines_removed', sa.Integer),
        sa.Column('bug', sa.Integer)
    )

    op.create_table(
        'radon_complexity_details',
        sa.Column('name', sa.VARCHAR),
        sa.Column('module_name', sa.VARCHAR),
        sa.Column('entity_name', sa.VARCHAR),
        sa.Column('type', sa.VARCHAR),
        sa.Column('complexity', sa.Integer),
        sa.Column('rank', sa.VARCHAR),
        sa.Column('indentation', sa.Integer),
        sa.Column('classname', sa.VARCHAR)
    )

    op.create_table(
        'radon_raw_metrics',
        sa.Column('name', sa.VARCHAR),
        sa.Column('module_name', sa.VARCHAR),
        sa.Column('loc', sa.Integer),
        sa.Column('lloc', sa.Integer),
        sa.Column('single_comments', sa.Integer),
        sa.Column('sloc', sa.Integer),
        sa.Column('multi', sa.Integer),
        sa.Column('comments', sa.Integer),
        sa.Column('blank', sa.Integer)
    )


def downgrade():
    op.drop_table('pylint_metrics')
    op.drop_table('pylint_metrics_by_msg')
    op.drop_table('git_metrics')
    op.drop_table('radon_complexity_details')
    op.drop_table('radon_raw_metrics')
