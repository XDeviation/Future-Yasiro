import yaml
from logger import Logger

logger = Logger(__name__, log_file="db_models.log")

logger.info("start loading config")
with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream).get("mq_config", {})
    except yaml.YAMLError as exc:
        logger.exception(exc)
        raise

MQ_HOST = config.get("host", "localhost")

logger.debug(f"MQ_HOST: {MQ_HOST}")
logger.info("load config success")
