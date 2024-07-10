import logging

from .env import AppEnv

logging.basicConfig(
    level=AppEnv.LOGGING_LEVEL,
    format="%(asctime)s - %(levelname)s - %(" "message)s",
)
logger: logging.Logger = logging.getLogger()
