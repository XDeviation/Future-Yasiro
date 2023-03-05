from typing import Dict, Union, List, Any
from logger import Logger
from ..qq_bot import QQMessageSender


logger = Logger(__name__, log_file="bot_controller.log")


class FakeBot:
    def send_group_message(
        self,
        id: str,
        message: Union[List[Dict[str, Any]], str],
        auto_escape=False,
    ) -> bool:
        return True

    def send_private_message(
        self,
        id: str,
        message: Union[List[Dict[str, Any]], str],
        auto_escape=False,
    ) -> bool:
        return True

    def send_message(self, message: Union[List[Dict[str, Any]], str]) -> bool:
        return True


class BotController:
    @classmethod
    def create(cls):

        logger.info("init BotController")

        controller = BotController()
        qq_bot = QQMessageSender.create()
        controller.bots["qq_message"] = qq_bot

        return controller

    def __init__(self):
        self.bots = {}

    def send_message(self, message: Dict[str, Any]) -> None:
        """
        send message to group
        :param message:
            :message_type: "qq_message"
            :message: Union[List[Dict[str, Any]], str]
        :return:
        """
        message_type = message["message_type"]
        _message = message["message"]
        logger.info(f"Send {message_type}")
        logger.info(self.bots)
        bot = self.bots.get(message_type, FakeBot())
        bot.send_message(_message)
