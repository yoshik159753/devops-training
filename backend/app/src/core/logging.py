import sys
from logging import DEBUG
from logging import Formatter as logFormatter
from logging import StreamHandler, getLevelName, getLogger

from src.core import config

handler = StreamHandler(stream=sys.stderr)
handler.setLevel(DEBUG)
handler.setFormatter(logFormatter('%(asctime)s - %(name)s - %(levelname)s - %(pathname)s(%(lineno)d) - %(message)s'))
logger = getLogger(config.PROJECT_NAME)
logger.setLevel(getLevelName(config.LOGGER_LEVEL))
logger.addHandler(handler)
