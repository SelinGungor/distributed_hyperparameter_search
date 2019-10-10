import pika
import logging
from config import get_config

logging.basicConfig(level=logging.DEBUG)
# reduce log level
logging.getLogger("pika").setLevel(logging.WARNING)

# disable propagation
logging.getLogger("pika").propagate = False

config = get_config("queue")


def get_connection():
    connection_uri = config['rabbitmq_uri']
    parameters = pika.URLParameters(connection_uri)
    logging.info(" parameters:" + str(parameters))
    connection = pika.BlockingConnection(parameters)
    logging.info("Creating a connection:" + str(connection))
    channel = connection.channel()
    return connection, channel
