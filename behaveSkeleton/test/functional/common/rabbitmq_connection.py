import logging
import pika
from behave import fixture

connection_params = pika.ConnectionParameters('localhost', 8080, pika.PlainCredentials('user', 'password'))

connection = pika.BlockingConnection(connection_params)


def connect_to_rabbit():
   
   connection = connection.channel()

   if connection == True:
    return "connected"
   else:
    return connection

def rabbit_publish(connection):

    connection.queue_declare(queue='output')


    connection.basic_publish(exchange='', routing_key='output', body='Hello RabbitMQ!')

    print("Sent 'Hello RabbitMQ!'")

    return f'published message'

def close_rabbit_connection():

    connection.close()


@fixture
def rabbitmq_connector(context):

    rabbitmq_connector = connect_to_rabbit()
    context.rabbitmq_connector = rabbitmq_connector

    return rabbitmq_connector
