import os
import json

from google.cloud import Storage as gcs

DESCRIPTION='description'
PRICE='price'
UPC='upc'
PRODUCT_FILE_NAME='PRODUCT_FILE_NAME'

class Validate(object):

    def __init__(self):
        self.client = gcs.Client()


    def validate_data(self, event):
        file_name = os.environ.get(PRODUCT_FILE_NAME)
        
        if file_name == event['file']:
            gcs_file = self.client.open(file_name)
            contents = gcs_file.read() 
        
            print(contents)

        return 'OK'
        