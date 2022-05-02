"""add pylint summary and by-msg metrics to number bugs views

Revision ID: 4aa9e6e6f5e5
Revises: 7e6997277a05
Create Date: 2019-02-23 05:40:18.649596

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4aa9e6e6f5e5'
down_revision = '7e6997277a05'
branch_labels = None
depends_on = None

sql_pylint_by_msg_to_bugs = '''SELECT 
                                    git_metrics.module_name,
                                    pylint_metrics_by_msg.msg,
                                    sum(pylint_metrics_by_msg.n) AS n,
                                    sum(git_metrics.bug) AS n_bugs
                                FROM 
                                    git_metrics, pylint_metrics_by_msg
                                WHERE 
                                    git_metrics.module_name::text = pylint_metrics_by_msg.module_name::text
                                GROUP BY 
                                    git_metrics.module_name, pylint_metrics_by_msg.msg
                                '''
sql_pylint_C_R_bugs = '''SELECT
                            git_metrics.module_name,
                            sum(pylint_metrics.n_convention) AS c,
                            sum(pylint_metrics.n_refactor) AS r,
                            sum(git_metrics.bug) AS bugs
                         FROM 
                            pylint_metrics, git_metrics
                         WHERE 
                            pylint_metrics.name::text = git_metrics.name::text AND 
                            pylint_metrics.module_name::text = git_metrics.module_name::text
                         GROUP BY 
                            git_metrics.module_name'''

CREATE_VIEW = '''CREATE VIEW {view_name} AS ({select_sql})'''
DROP_VIEW = '''DROP VIEW {view_name}'''


def upgrade():
    op.execute(CREATE_VIEW.format(view_name='v_pylint_by_msg_to_bugs',
                                  select_sql=sql_pylint_by_msg_to_bugs))
    op.execute(CREATE_VIEW.format(view_name='v_pylint_C_R_bugs',
                                  select_sql=sql_pylint_C_R_bugs))


def downgrade():
    op.execute(DROP_VIEW.format(view_name='v_pylint_by_msg_to_bugs'))
    op.execute(DROP_VIEW.format(view_name='v_pylint_C_R_bugs'))
    pass
