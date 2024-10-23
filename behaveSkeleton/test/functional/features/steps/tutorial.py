from behave import *
import test.functional.common.rabbitmq_connection as mq
import json
from comm  file_walker

@given('the normaliser is running')
def step_impl(context):
    pass

@when('the normaliser receives a {data_type} payload')
def step_impl(context, data_type):
    step_data = json.loads(context.text)
    
    expected_input_filename = step_data['input']

    file_path = f'test/functional/common/fixtures/test_data/input/{expected_input_filename}'

    # file_contents = open(file=f'{expected_input_filepath}')
    # next: file walker to monitor the input dir
    # next: use xmltodict to parse xml to a dict format
    # next: pass dict as message to rabbit
    # next: assert expected == actual
    message = file_walker(file_path)
    print(message)

    # connection = mq.connect_to_rabbit()

    # mq.rabbit_publish(connection, message)




@then('it should convert the fixture data into a JSON payload')
def step_impl(context):
    pass    

@then('sent it to RabbitMQ to be ingested')
def step_impl(context):
    pass