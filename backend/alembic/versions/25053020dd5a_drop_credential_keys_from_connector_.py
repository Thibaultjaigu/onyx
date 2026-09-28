"""drop credential keys from connector configs

Revision ID: 25053020dd5a
Revises: ac05f4a21dbd
Create Date: 2026-09-28 12:00:16.352326

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "25053020dd5a"
down_revision = "ac05f4a21dbd"
branch_labels = None
depends_on = None

# These connectors no longer accept these keys as config kwargs;
# load_credentials always set them from the credential instead.
REMOVED_KEYS_BY_SOURCE: dict[str, list[str]] = {
    "CLICKUP": ["api_token", "team_id"],
    "HUBSPOT": ["access_token"],
    "DOCUMENT360": ["api_token", "portal_id"],
    "GURU": ["guru_user", "guru_user_token"],
}


def upgrade() -> None:
    conn = op.get_bind()
    for source, keys in REMOVED_KEYS_BY_SOURCE.items():
        for key in keys:
            conn.execute(
                sa.text(
                    "UPDATE connector "
                    "SET connector_specific_config = connector_specific_config - :key "
                    "WHERE source = :source AND connector_specific_config ? :key"
                ),
                {"source": source, "key": key},
            )


def downgrade() -> None:
    # The removed values were always overwritten by the credential, so there is nothing to restore.
    pass
