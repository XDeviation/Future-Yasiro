import yaml
from logger import Logger

logger = Logger(__name__, log_file="im_rec.log")

logger.info("start loading config")
with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream).get("rec_server_config", {})
    except yaml.YAMLError as exc:
        logger.exception(exc)
        raise

REC_SERVER_PORT = config.get("port", 3500)

logger.info("load config success")
