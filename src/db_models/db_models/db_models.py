import datetime
from logger import Logger
from functools import wraps
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, TEXT, TIMESTAMP, create_engine, BigInteger

from db_models.config import DB_URL

base = declarative_base()
logger = Logger(__name__, log_file="db_models.log")


class SendMessage(base):
    __tablename__ = "send_message"
    message_id = Column(BigInteger, primary_key=True)
    plugin_name = Column(TEXT)
    message = Column(TEXT)
    time = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class PluginToUser(base):
    __tablename__ = "plugin_to_user"
    id = Column(BigInteger, primary_key=True)
    plugin_name = Column(TEXT)
    user_type = Column(TEXT)
    user_id = Column(TEXT)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


def provide_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        engine = create_engine(DB_URL)
        Session = sessionmaker(bind=engine)
        session = Session()
        return func(session, *args, **kwargs)

    return wrapper
