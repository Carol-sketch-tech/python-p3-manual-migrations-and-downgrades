"""renanming the table fro students to scholars

Revision ID: a4d9031ca47f
Revises: 791279dd0760
Create Date: 2024-09-19 15:28:42.077476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4d9031ca47f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('students','scholars')
