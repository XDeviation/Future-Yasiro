from logger import Logger
from db_models import provide_session, Message
from sqlalchemy.orm import Session
from qq_bot import QQMessageSender

logger = Logger(__name__, log_file="bot_controller.log")


@provide_session
def get_message(session: Session):
    res = session.query(Message).one_or_none()
    logger.info(res.to_dict())
    return res


if __name__ == "__main__":
    get_message()
