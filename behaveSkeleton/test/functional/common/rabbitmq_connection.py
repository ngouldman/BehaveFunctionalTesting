import logging
import pika
from behave import fixture
import pika.exceptions



def connect_to_rabbit():

    connection_params = pika.ConnectionParameters('rabbitmq', 5672, '/')

    connection = pika.BlockingConnection(connection_params)

    channel = connection.channel()

    return channel

   
def rabbit_publish(channel, message=None):

    channel.queue_declare(queue='normaliser')

    channel.basic_publish(exchange='inbound', routing_key='output', body=message)

    return channel

# def rabbit_get_message(channel):

def close_rabbit_connection(channel):

    channel.close()


@fixture
def rabbitmq_connector(context):

    rabbitmq_connector = connect_to_rabbit()
    context.rabbitmq_connector = rabbitmq_connector

    return rabbitmq_connector
