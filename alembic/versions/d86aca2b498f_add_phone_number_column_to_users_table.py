"""add phone number column to users table

Revision ID: d86aca2b498f
Revises: 46b5c8c4971d
Create Date: 2026-06-19 22:03:53.274347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd86aca2b498f'
down_revision: Union[str, Sequence[str], None] = '46b5c8c4971d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
