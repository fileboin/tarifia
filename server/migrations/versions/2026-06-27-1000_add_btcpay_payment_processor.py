"""Add btcpay as a supported payment processor

Revision ID: f1a2b3c4d5e6
Revises: e7118c4ae5d8
Create Date: 2026-06-27 10:00:00.000000

The ``payment_processor`` column on ``checkouts`` and ``checkout_links`` is a
plain VARCHAR, so no DDL change is required.  This migration is intentionally
a no-op — it exists only to record the introduction of the ``btcpay`` value in
the version history.
"""

# revision identifiers, used by Alembic.
revision = "f1a2b3c4d5e6"
down_revision = "e7118c4ae5d8"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
