import os
from services.validate_data import Validate

validate = Validate()

def validate_products(event, context):

    response = validate.validate_data(event)


    return "Hello World!" 