"""
This is a example plugin
When user send ".help" to bot, bot will return help
"""

import json

# import Future Yasiro improve package
from logger import Logger
from mq_utils import get_mq_connection

# You can find your log in src/logs/{log_file}
logger = Logger(__name__, log_file="help.log")

help_message = """Welcome use Future Yasiro!
.help get help"""

def main():
    mq_connection = get_mq_connection()
    mq_channel = mq_connection.channel()
    mq_channel.queue_declare(queue=".help")


    def callback(ch, method, properties, body):
        message = json.loads(body)
        message_type = message.get("message_type", "")
        if message_type != 'private' and message_type != 'group':
            return

        send_mq_connection = get_mq_connection()
        send_mq_channal = send_mq_connection.channel()
        send_mq_channal.queue_declare(queue="send_message")
        return_msg = {
            "message_type": "qq_message",
            "message": None,
        }
        if message_type == 'private':
            user_id = message.get("user_id", 0)
            return_msg["message"] = { 
                "action": "send_private_msg",
                "params": {
                    "user_id": user_id, 
                    "message": help_message,
                    "auto_escape": True
                }
            }
            

        if message_type == 'group':
            group_id = message.get("group_id", 0)
            return_msg["message"] = { 
                "action": "send_group_msg",
                "params": {
                    "group_id": group_id, 
                    "message": help_message,
                    "auto_escape": True
                }
            }

        send_mq_channal.basic_publish(
            exchange='',
            routing_key="send_message",
            body=json.dumps(return_msg)
        )
        logger.info(f"Send message {return_msg}")

    mq_channel.basic_consume(
        queue=".help", on_message_callback=callback, auto_ack=True
    )
    mq_channel.start_consuming()

    mq_connection.close()
