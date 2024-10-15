from common.rabbitmq_connection import connect_to_rabbit, close_rabbit_connection

from behave import use_fixture

def before_all(context, tag):

    if tag == "fixture.rabbitmq_connector":
        use_fixture(connect_to_rabbit, context)
    

def after_scenario(context, scenario):
   close_rabbit_connection()