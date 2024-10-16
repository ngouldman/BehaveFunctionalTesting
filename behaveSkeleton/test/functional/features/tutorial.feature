@fixture.rabbitmq

Feature: POC connecting to rabbit

Scenario Outline: Fixture XML data is successfully sent to the normaliser and transformed into a JSON payload 
     Given the normaliser is running
     When the normaliser receives a fixture payload
      """
        {
        "input": "<input_filename>"
        }
      """
     Then it should convert the fixture data into a JSON payload
     And sent it to RabbitMQ to be ingested
     Examples:
     |scenario | input_filename | output_filename | 
      # | error queue        | |
     | put data into a queue | data_into_queue.xml | |
      # | ingest data into DB | | 