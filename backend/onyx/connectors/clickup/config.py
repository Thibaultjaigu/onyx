from enum import StrEnum

from onyx.configs.app_configs import INDEX_BATCH_SIZE
from onyx.connectors.connector_config import ConnectorConfig


class ClickupConnectorType(StrEnum):
    LIST = "list"
    FOLDER = "folder"
    SPACE = "space"
    WORKSPACE = "workspace"


class ClickupConnectorConfig(ConnectorConfig):
    batch_size: int = INDEX_BATCH_SIZE
    connector_type: ClickupConnectorType | None = None
    connector_ids: list[str] | None = None
    retrieve_task_comments: bool = True
