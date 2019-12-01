import json
import os 

from google.cloud import storage as gcs

VALID_PRODUCTS_BUCKET_NAME='VALID_PRODUCTS_BUCKET_NAME'
INVALID_PRODUCTS_BUCKET_NAME='INVALID_PRODUCTS_BUCKET_NAME'
VALID_FILE_NAME='VALID_FILE_NAME'
INVALID_FILE_NAME='INVALID_FILE_NAME'


class StorageClient(object):

    def __init__(self):
        self.client = gcs.Client()
        self.valid_bucket_name = os.environ.get(VALID_PRODUCTS_BUCKET_NAME)
        self.invalid_bucket_name = os.environ.get(INVALID_PRODUCTS_BUCKET_NAME)
        self.valid_file_name = os.environ.get(VALID_FILE_NAME)
        self.invalid_file_name = os.environ.get(INVALID_FILE_NAME)


    def get_gcs_client(self):
        return self.client

    
    def get_data(self, bucket_name, file_name):
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.get_blob(file_name)

        return json.loads(blob.download_as_string())


    def upload_to_gcs(self, valid_file_path, invalid_file_path):
        try:
            self.client.create_bucket(self.valid_bucket_name)
            self.client.create_bucket(self.invalid_bucket_name)

            self.__upload_file(self.valid_bucket_name, valid_file_path, self.valid_file_name)
            self.__upload_file(self.invalid_bucket_name, invalid_file_path, self.invalid_file_name)
        except:
            print("Error!")


    def __upload_file(self, bucket_name, file_path, file_name):
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(file_name)

            blob.upload_from_filename(
                file_path
            )

            url = blob.public_url

            return url
        except Exception as e:
            print(e)
