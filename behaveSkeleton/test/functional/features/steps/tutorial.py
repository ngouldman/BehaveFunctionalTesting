from behave import *
import json


@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    pass

@then('behave will test it for us!')
def step_impl(context):
    step_data = json.loads(context.text)
    
    expected_output_filename = step_data['expected']

    expected_output_filepath = f'output/{expected_output_filename}'

    connector = context.rabbit_connector

    print('hello', connector)

    # assert we get an output message in the output queue