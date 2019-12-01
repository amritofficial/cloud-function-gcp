# About the project

The project makes use of Google Cloud Function to respond to a file upload event on Google Storage Bucket and does the file processing and uploading those files to two new buckets

## Getting Started

The bucket is a standard `regional` setup with zone as `us-central1` (Montreal) and uses uniform bucket-level access

## Prerequisites

What things you need to install the software and how to install them


```
gcloud
```
```
python3.7
```

### Installing and Deployment

To run the project, the user could simply run the following command that would deploy code to Google Cloud Function


1. Change directory to enter `validate_products` directory
```
cd functions/validate_products
```

Note: Make sure you have `.env.yaml` file inside `validate_products` directory, the file will be used to set all the environment variables

2. Run the following command to deploy the cloud function. Follow Google Cloud Storage Documentation for more details

```
gcloud functions deploy function-validate-file --runtime python37 --env-vars-file .env.yaml --trigger-bucket product-consumables
```


## Triggering the Cloud Function

Upload a file to Google Cloud Storage bucket `product-consumables`, it will trigger the event


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc