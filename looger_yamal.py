import logging
import yaml
import logging.config

with open('config.yaml','r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
logger.debug('this is debug message')