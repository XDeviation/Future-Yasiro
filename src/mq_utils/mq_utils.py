import pika
from . import pika_pool
from logger import Logger
from .config import MQ_HOST

logger = Logger(__name__, log_file="mq_utils.log")

POOL = pika_pool.QueuedPool(
    create=lambda: pika.BlockingConnection(pika.ConnectionParameters(MQ_HOST)),
    max_size=50,
    max_overflow=10,
    recycle=60,
    timeout=10,
)
logger.info("Create pool successfully")


def get_mq_connection():
    return pika.BlockingConnection(pika.ConnectionParameters(MQ_HOST))
