"""create users and screenplays

Revision ID: 7c25523b9fa4
Revises:
Create Date: 2026-05-13 11:16:12.665868

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7c25523b9fa4"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "screenplays",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("author_id", sa.BIGINT(), nullable=False),
        sa.Column("title", sa.String(length=75), nullable=False),
        sa.Column("logline", sa.String(length=40), nullable=True),
        sa.Column("redacted_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("author_id", "title", name="author_title_uq"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("screenplays")
    op.drop_table("users")
