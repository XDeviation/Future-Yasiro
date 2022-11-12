import requests
from typing import Dict, Union
from .config import QQ_BOT_API_URL
from logger import Logger


logger = Logger(__name__, log_file="qq_bot.log")


class QQMessageSender:
    def __init__(self):
        logger.info("init QQMessageSender")

    def send_group_message(
        self, group_id: int, message: Union[Dict, str], auto_escape=False
    ):
        """
        send message to group
        :param group_id: group_id
        :param message: https://12.onebot.dev/interface/message/type
        :param auto_escape: whether send message as text
        :return:
        """
        on_auto_escape = "On" if auto_escape else "Off"
        url = f"http://{QQ_BOT_API_URL}/send_group_msg"
        logger.info(
            f"[Auto Escape {on_auto_escape}] send message to group {group_id}: {message}"
        )
        try:
            res = requests.post(
                url,
                json={
                    "group_id": group_id,
                    "message": message,
                    "auto_escape": auto_escape,
                },
            )
        except Exception as e:
            logger.exception(f"send message to group {group_id} failed: {e}")
            return
        if res.status_code != 200:
            logger.error(f"send message to group {group_id} failed: {res.text}")
            return
        logger.info(f"send message to group {group_id} success: {res.text}")


if __name__ == "__main__":
    bot = QQMessageSender()
    bot.send_group_message(123456, "test", True)
