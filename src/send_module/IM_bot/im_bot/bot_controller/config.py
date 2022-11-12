import yaml
from logger import Logger

logger = Logger(__name__, log_file="bot_controller.log")

logger.info("start loading config")
with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream).get("db_config", {})
    except yaml.YAMLError as exc:
        logger.exception(exc)
        raise

DB_HOST = config.get("host", "localhost")
DB_PORT = config.get("port", 5432)
DB_USER = config.get("user", "root")
DB_PASSWORD = config.get("password", "postgres")
DB_NAME = config.get("database", "default")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

logger.debug(f"DB_URL: {DB_URL}")
logger.info("load config success")
