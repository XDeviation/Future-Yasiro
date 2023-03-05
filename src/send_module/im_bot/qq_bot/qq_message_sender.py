import requests
from typing import Dict, Union, List, Any
from .config import QQ_BOT_API_URL, QQ_MASTER
from logger import Logger


logger = Logger(__name__, log_file="qq_bot.log")


class QQMessageSender:
    @classmethod
    def create(cls):
        logger.info("init QQ bot module")

        bot = QQMessageSender()

        retries = 3
        while retries:
            retries -= 1
            res = bot.send_private_message(
                id=bot.master,
                message=[{"type": "text", "data": {"text": "link start!"}}],
                auto_escape=False,
            )
            if res:
                bot.alive = True
                logger.info(f"Init QQ bot module sussfully")
                return bot

        logger.error(
            f"Can't send message to master, QQ bot module will not be available."
        )

        return bot

    def __init__(self):
        self.endpoint = f"http://{QQ_BOT_API_URL}"
        self.master = QQ_MASTER
        self.alive = True
        self.funcs = {
            "send_group_msg": self.send_group_message,
            "send_private_msg": self.send_private_message,
        }

    def send_group_message(
        self,
        id: str,
        message: Union[List[Dict[str, Any]], str],
        auto_escape=False,
    ) -> bool:
        """
        send message to group
        :param id: group_id
        :param message: https://12.onebot.dev/interface/message/type
        :param auto_escape: whether send message as text
        :return: whether commend success
        """
        if not self.alive:
            return False

        group_id = int(id)
        on_auto_escape = "On" if auto_escape else "Off"
        logger.debug(
            f"[Auto Escape {on_auto_escape}] send message to group {group_id}: {message}"
        )

        url = f"{self.endpoint}/send_group_msg"
        params = {
            "group_id": group_id,
            "message": message,
            "auto_escape": auto_escape,
        }
        res = requests.post(
            url,
            json=params,
        )

        if res.status_code != 200:
            logger.error(
                f"send message {message} with auto escape {on_auto_escape} to group {group_id} failed: {res.text}"
            )
            return False
        logger.debug(f"send message to group {group_id} success: {res.text}")

    def send_private_message(
        self,
        id: str,
        message: Union[List[Dict[str, Any]], str],
        auto_escape=False,
    ) -> bool:
        """
        send message to user
        :param id: user_id
        :param message: https://12.onebot.dev/interface/message/type
        :param auto_escape: whether send message as text
        :return: whether commend success
        """
        if not self.alive:
            return False
        user_id = int(id)
        on_auto_escape = "On" if auto_escape else "Off"
        url = f"{self.endpoint}/send_private_msg"
        logger.debug(
            f"[Auto Escape {on_auto_escape}] send message to user {user_id}: {message}"
        )
        params = {
            "user_id": user_id,
            "message": message,
            "auto_escape": auto_escape,
        }
        res = requests.post(
            url,
            json=params,
        )

        if res.status_code != 200:
            logger.error(
                f"send message {message} to endpoint {self.endpoint} with auto escape {on_auto_escape} to user {user_id} failed: {res.text}"
            )
            return False
        logger.debug(f"send message to user {user_id} success: {res.text}")
        return True

    def send_message(self, message: Union[List[Dict[str, Any]], str]):
        url = self.endpoint
        logger.debug(f"send message with params: {message}")
        res = requests.post(
            url,
            json=message,
        )
        if res.status_code != 200:
            logger.debug(
                f"send message with params: \n ----------- \n{message}\n----------\n failed: {res.text}"
            )
            return False

        return True
