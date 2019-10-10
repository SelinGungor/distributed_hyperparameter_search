import pika
from typing import List
import logging
from config import get_config

logging.basicConfig(level=logging.DEBUG)
# reduce log level
logging.getLogger("pika").setLevel(logging.WARNING)

# or, disable propagation
logging.getLogger("pika").propagate = False

config = get_config('queue')


def get_connection():
    connection_uri = config['rabbitmq_uri']
    parameters = pika.URLParameters(connection_uri)
    logging.info(" parameters:" + str(parameters))
    connection = pika.BlockingConnection(parameters)
    logging.info(" connection:" + str(connection))
    channel = connection.channel()
    return connection, channel


def close_connection(connection):
    connection.close()


def publish_to_queue(parameters: List[str]):
    try:
        connection, channel = get_connection()

        exchange_name = config['exchange_name']
        queue_name = config['queue_name']
        routing_key = config['routing_key']
        logging.info('Publishing messages with routing_key :' + routing_key)

        channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
        channel.queue_declare(queue_name)

        channel.queue_bind(exchange=exchange_name,
                           queue=queue_name,
                           routing_key=routing_key)
        for message in parameters:
            channel.basic_publish(
                exchange=exchange_name, routing_key=routing_key, body=message)
            logging.info("Message sent! %r" % message)
    finally:
        close_connection(connection)





