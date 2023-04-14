import yaml
from logger import Logger

logger = Logger(__name__, log_file="qq_bot.log")

logger.info("start loading config")
with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream).get("qq_config", {})
    except yaml.YAMLError as exc:
        logger.exception(exc)
        raise

QQ_MASTER = config.get(
    "master", None
)  # QQ master, when init QQ bot will send a message to this ID
QQ_BOT_API_HOST = config.get("host", "localhost")
QQ_BOT_API_PORT = config.get("port", 8080)
QQ_BOT_API_URL = f"{QQ_BOT_API_HOST}:{QQ_BOT_API_PORT}"

logger.info("load config success")
