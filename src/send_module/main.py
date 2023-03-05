import json

from .im_bot import BotController
from logger import Logger
from mq_utils import get_mq_connection

logger = Logger(__name__, log_file="send_message.log")

def main():
    mq_connection = get_mq_connection()
    mq_channel = mq_connection.channel()
    mq_channel.queue_declare(queue="send_message")

    bot_controller = BotController.create()

    def callback(ch, method, properties, body):
        message = json.loads(body)
        logger.debug(f"Receive send message request: {message}")
        bot_controller.send_message(message)

    mq_channel.basic_consume(
        queue="send_message", on_message_callback=callback, auto_ack=True
    )
    mq_channel.start_consuming()

    mq_connection.close()
