from logger import Logger
from db_models.db_models import provide_session, Message
from sqlalchemy.orm import Session
from im_bot.qq_bot.send_message import QQMessageSender


logger = Logger(__name__, log_file="bot_controller.log")


class BotController:
    @classmethod
    async def create(cls):
        logger.info("init BotController")

        self = BotController()

        qq_bot = await QQMessageSender.create()
        self.bots.append(qq_bot)

    def __init__(self):
        self.bots = []

    @provide_session
    def get_message(session: Session, self, message_id: int) -> Message:
        """
        get message from database
        :param session:
        :return:
        """
        message = session.query(Message).first()
        if message:
            session.delete(message)
            session.commit()
        return message

    def send_group_message(self, message: Message):
        """
        send message to qq group
        :param message:
        :return:
        """
        for bot in self.bots:
            bot.send_group_message(message.message_id, message.message, False)
