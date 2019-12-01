import os
import json
import math

from google.cloud import storage as gcs

from services.validate_data import Validate

PRODUCT_FILE_NAME='PRODUCT_FILE_NAME'
BUCKET_NAME='BUCKET_NAME'


class ProcessFile(object):

    def __init__(self):
        self.validate = Validate()
        # self.client = gcs.Client()


    def process_file(self, event):
        # bucket_name = os.environ.get(BUCKET_NAME)
        # file_name = os.environ.get(PRODUCT_FILE_NAME)
        
        # if file_name == event['name']:
        #     bucket = self.client.get_bucket(bucket_name)
        #     blob = bucket.get_blob(file_name)

            # data = json.loads(blob.download_as_string())
        with open(os.path.join(os.getcwd(), 'services/products.json'), 'r') as stream:
            data = json.load(stream)
            self.__filter_data(data)
            # print(json.loads(file))
            # print(data)

        return 'OK'


    def __filter_data(self, data):
        invalid = {}
        valid = {}
        for key in data.keys():
            invalid[key] = []
            valid[key] = []
            for value in data[key]:
                valid_flag = self.validate.validate_data(value)
                if not valid_flag:
                    invalid[key].append(value)
                else:
                    valid[key].append(value)

    