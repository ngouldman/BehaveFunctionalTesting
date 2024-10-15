@fixture.rabbitmq_connector

Feature: POC connecting to rabbit

Scenario Outline: run a simple test
     Given we have behave installed
     When we implement a test
     Then behave will test it for us!
       """
        {
        "expected": "<output_filename>"
        }
      """
     Examples:
     |scenario | output_filename |
      # | error queue        | |
     | put data into a queue | data_into_queue.json |
      # | ingest data into DB | | 