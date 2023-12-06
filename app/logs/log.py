import logging
from os import getenv

level = getenv("LOG_LEVEL")
if not level:
    raise OSError("LOG_LEVEL environment variable is required")
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    level=logging.getLevelName(level),
)
logger = logging.getLogger(__name__)
