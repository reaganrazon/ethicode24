"""empty message

Revision ID: afcddb178576
Revises: 3ff7862f182c
Create Date: 2024-02-17 10:30:23.633431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'afcddb178576'
down_revision: Union[str, None] = '3ff7862f182c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lessonplan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('filemodel')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('filemodel',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('filename', sa.VARCHAR(), nullable=False),
    sa.Column('content', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('lessonplan')
    # ### end Alembic commands ###