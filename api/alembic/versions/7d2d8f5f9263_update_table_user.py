"""Update table user

Revision ID: 7d2d8f5f9263
Revises: b4b1eca055dd
Create Date: 2025-04-15 20:26:01.960032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d2d8f5f9263'
down_revision: Union[str, None] = 'b4b1eca055dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('country_code', sa.String(length=2), nullable=False))
    op.add_column('users', sa.Column('phone_number', sa.String(length=11), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'country_code')
    # ### end Alembic commands ###
