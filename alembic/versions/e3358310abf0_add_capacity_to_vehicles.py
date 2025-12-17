"""Add user auth fields (is_email_verified, timestamps)

Revision ID: e3358310abf0
Revises: 2e37c0074375
Create Date: 2025-12-17 09:27:07.051860

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e3358310abf0"
down_revision: Union[str, Sequence[str], None] = "2e37c0074375"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add new columns to users table
    op.add_column(
        "users",
        sa.Column(
            "is_email_verified", sa.Boolean(), nullable=False, server_default="0"
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "updated_at")
    op.drop_column("users", "created_at")
    op.drop_column("users", "is_email_verified")
