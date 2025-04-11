"""Adjuste question

Revision ID: b4b1eca055dd
Revises: 94373e785e15
Create Date: 2025-04-10 21:53:18.699371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4b1eca055dd'
down_revision: Union[str, None] = '94373e785e15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('question', sa.String(length=255), nullable=False))
    op.add_column('questions', sa.Column('response', sa.String(), nullable=True))
    op.drop_column('questions', 'title')
    op.drop_column('questions', 'content')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('questions', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('questions', 'response')
    op.drop_column('questions', 'question')
    # ### end Alembic commands ###
