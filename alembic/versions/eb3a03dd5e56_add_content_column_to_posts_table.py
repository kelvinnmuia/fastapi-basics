"""add content column to posts table

Revision ID: eb3a03dd5e56
Revises: eec4181e614d
Create Date: 2026-06-19 17:24:05.958798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb3a03dd5e56'
down_revision: Union[str, Sequence[str], None] = 'eec4181e614d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
