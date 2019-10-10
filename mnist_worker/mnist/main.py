from data.read_data import read_data
from model.keras_mnist import evaluate_model
from db.result import Result
from queue_connection import get_connection
import sys
import datetime
from config import get_config
import json
import logging

pod_name = "some_pod_name"

x_train, y_train, x_test, y_test, input_shape = read_data()


def evaluate(hyperparameters):
    logging.info("This is the start " + str(hyperparameters) + " This is the end")

    starting_time = datetime.datetime.now()
    evaluation_result = evaluate_model(x_train, y_train, x_test, y_test, input_shape, hyperparameters)
    time_spent = datetime.datetime.now() - starting_time

    logging.info("Evaluation result is: " + str(evaluation_result))

    # insert into the database
    item = Result(hyperparameters_value=hyperparameters, pod_name=pod_name, time_spent=time_spent,
                  results=evaluation_result)

    logging.info("Result item: " + str(item))

    item.save()

    return True


def receive_logs():
    connection, channel = get_connection()
    config = get_config("queue")

    binding_keys = config['binding_keys']
    exchange_name = config['exchange_name']
    queue_name = config['queue_name']

    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

    result = channel.queue_declare(queue_name)
    queue_name = result.method.queue
    logging.info("Queue name is " + queue_name)

    if not binding_keys:
        sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(
            exchange=exchange_name, queue=queue_name, routing_key=binding_key)

    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body))
        hyperparameter = json.loads(body)
        evaluate(hyperparameters=hyperparameter)
        logging.info("Completed!" + queue_name)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':
    receive_logs()
