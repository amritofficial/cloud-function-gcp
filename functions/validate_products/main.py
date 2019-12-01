import os
from controllers.process_file import ProcessFile

process_file = ProcessFile()


def validate_products(event, context):
    response = process_file.process_file(event)

    return "Hello World!" 
