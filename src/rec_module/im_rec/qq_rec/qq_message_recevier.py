import re
import json
from fastapi import APIRouter, Request
from logger import Logger
from mq_utils import get_mq_connection

logger = Logger(__name__, log_file="im_rec.log")
router = APIRouter()

@router.post("/qq_rec")
async def qq_rec(req: Request):
    message = await req.json()
    logger.debug(f"Rec message: {message}")
    post_type = message.get("post_type", "")
    message_detail = message.get("message", "")
    if post_type != 'message' or not message_detail.startswith('.'):
        return {}
    try:
        message_queue = re.split(' |\n|\t', message_detail)[0]

        logger.info(f"Receive command {message_queue}, send it to queue")
        queue_connection = get_mq_connection()
        channel = queue_connection.channel()
        channel.queue_declare(queue=message_queue)
        channel.basic_publish(exchange='',
                        routing_key=message_queue,
                        body=json.dumps(message))
        logger.info(f"Done.")
    except Exception as e:
        logger.exception(e)
        return {}
    return {}