"""add content column to posts table

Revision ID: 0775b16438f5
Revises: c5f109abe690
Create Date: 2023-10-22 21:12:24.792466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0775b16438f5"
down_revision: Union[str, None] = "c5f109abe690"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
