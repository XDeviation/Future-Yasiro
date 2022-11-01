import datetime
from email.policy import default
from logger import Logger
from functools import wraps
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, TEXT, TIMESTAMP, create_engine

base = declarative_base()
logger = Logger(__name__, log_file="bot_controller.log")


class Message(base):
    __tablename__ = "message"
    message_id = Column(TEXT, primary_key=True)
    plugin_id = Column(TEXT)
    plugin_key = Column(TEXT)
    plugin_secret = Column(TEXT)
    message = Column(JSONB)
    time = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


def provide_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        engine = create_engine(
            "postgresql://future_yasiro:adachisakura@localhost:5432/adachi_datas"
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        return func(session, *args, **kwargs)

    return wrapper
