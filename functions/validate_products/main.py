import os
from controllers.process_file import ProcessFile

process_file = ProcessFile()


def validate_products(event, context):
    """
    The function that gets executed when a file is uploaded to Google Cloud Storage (GCS)
    :param event: the event that gets triggered
    :param context: the event metadata
    """

    response = process_file.process_file(event)

    return "OK" 
