import json
import tempfile
from google.cloud import storage as gcs

class StorageClient(object):

    def __init__(self):
        self.client = gcs.Client()


    def get_gcs_client(self):
        return self.client

    
    def get_data(self, bucket_name, file_name):
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.get_blob(file_name)

        return json.loads(blob.download_as_string())


    def upload_to_gcs(self, valid_file, invalid_file):
        print("UPLOAD TO GCS")