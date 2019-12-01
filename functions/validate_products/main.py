import os
from services.process_file import ProcessFile

process_file = ProcessFile()

def validate_products(event, context):
    response = process_file.process_file(event)


    return "Hello World!" 


if __name__ == "__main__":
    process_file.process_file("")