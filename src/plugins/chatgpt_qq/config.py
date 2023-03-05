import yaml
# from logger import Logger

# logger = Logger(__name__, log_file="qq_bot.log")

# logger.info("start loading config")
with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream).get("chatgpt_config", {})
    except yaml.YAMLError as exc:
        # logger.exception(exc)
        raise

DATA_FILE = config.get("data_file", "")
CHATGPT_API_KEY = config.get("key", "")
TOKEN_LIMIT = config.get("token_limit", 4096)

# logger.info("load config success")