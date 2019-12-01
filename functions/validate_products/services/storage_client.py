import json
import os 

from google.cloud import storage as gcs

VALID_PRODUCTS_BUCKET_NAME='VALID_PRODUCTS_BUCKET_NAME'
INVALID_PRODUCTS_BUCKET_NAME='INVALID_PRODUCTS_BUCKET_NAME'
VALID_FILE_NAME='VALID_FILE_NAME'
INVALID_FILE_NAME='INVALID_FILE_NAME'


class StorageClient(object):

    def __init__(self):
        """
        A service class that does all the storage side jobs
        :param:
        :return: 
        """

        self.client = gcs.Client()
        self.valid_bucket_name = os.environ.get(VALID_PRODUCTS_BUCKET_NAME)
        self.invalid_bucket_name = os.environ.get(INVALID_PRODUCTS_BUCKET_NAME)
        self.valid_file_name = os.environ.get(VALID_FILE_NAME)
        self.invalid_file_name = os.environ.get(INVALID_FILE_NAME)

    
    def get_data(self, bucket_name, file_name):
        """
        The method retreives the data from the bucket given the filename
        :param bucket_name: the name of the bucket from where to retreive data 
        :param file_name: the name of the file 
        :return: user friendly json format of blob downloaded as a string & dumped
        """

        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.get_blob(file_name)

        return json.loads(blob.download_as_string())


    def upload_to_gcs(self, valid_file_path, invalid_file_path):
        """
        The method creates the bucket for valid and invalid products file
        :param valid_file_path: valid products file path of tmp directory
        :param invalid_file_path: invalid products file path of tmp directory
        :return: 
        """

        try:
            self.client.create_bucket(self.valid_bucket_name)
            self.client.create_bucket(self.invalid_bucket_name)

            self.__upload_file(self.valid_bucket_name, valid_file_path, self.valid_file_name)
            self.__upload_file(self.invalid_bucket_name, invalid_file_path, self.invalid_file_name)
        except:
            print("Error!")


    def __upload_file(self, bucket_name, file_path, file_name):
        """
        A standard reusable method to push the files to GCS buckets
        :param bucket_name: the name of the bucket to push files to
        :param file_path: the exact path of the file
        :param file_name: the name of the file to be pushed
        :return: url of the uploaded file to bucket
        """

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
