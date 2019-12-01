import os
import json
import math

from google.cloud import storage as gcs

from services.validate_data import Validate
from services.storage_client import StorageClient
from shared.utils import create_temp_file_path

PRODUCT_FILE_NAME='PRODUCT_FILE_NAME'
BUCKET_NAME='BUCKET_NAME'
VALID_PRODUCTS_BUCKET_NAME='VALID_PRODUCTS_BUCKET_NAME'
INVALID_PRODUCTS_BUCKET_NAME='INVALID_PRODUCTS_BUCKET_NAME'
VALID_FILE_NAME='VALID_FILE_NAME'
INVALID_FILE_NAME='INVALID_FILE_NAME'


class ProcessFile(object):

    def __init__(self):
        """
        Act as a controller and init all the variables used throughout this class
        """
        self.validate = Validate()
        self.storage_client = StorageClient()
        self.bucket_name = os.environ.get(BUCKET_NAME)
        self.file_name = os.environ.get(PRODUCT_FILE_NAME)
        self.valid_file_path = create_temp_file_path(os.environ.get(VALID_FILE_NAME))
        self.invalid_file_path = create_temp_file_path(os.environ.get(INVALID_FILE_NAME))


    def process_file(self, event):
        """
        A standard method of controller that runs all the different methods
        The methods calls different services to get the job done
        :param event: the file upload event that gets triggered
        """
        if self.file_name == event['name']:
            data = self.storage_client.get_data(self.bucket_name, self.file_name)
       
            valid = self.validate.filter_valid(data)
            invalid = self.validate.filter_invalid(data)

            with open(self.valid_file_path, 'w') as valid_file:
                json.dump(valid, valid_file)
            
            with open(self.invalid_file_path, 'w') as invalid_file:
                json.dump(valid, invalid_file)

            self.storage_client.upload_to_gcs(self.valid_file_path, self.invalid_file_path)

        return 'File Upload Success!'
