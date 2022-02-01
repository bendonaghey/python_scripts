import boto3
from datetime import datetime, timedelta

# def lambda_handler(event, context):

# Enter a list of buckets to copy from
buckets_list = ['']
destination_bucket = ''

s3_client = boto3.client('s3')


# Create a reusable Paginator
paginator = s3_client.get_paginator('list_objects_v2')

def iterate_s3_buckets(bucket_name):
    count = 0
    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket = bucket_name)

    # Loop through each object, looking for ones older than a given time period
    for page in page_iterator:  
        for object in page['Contents']:
            if object['LastModified'] < datetime.now().astimezone() - timedelta(days = 1):   # <-- Change time period here
                print(f"Moving {object['Key']} from {bucket_name} to {destination_bucket}")

                # Copy object
                s3_client.copy_object(
                    Bucket = destination_bucket,
                    Key = bucket_name + f"/{object['Key']}",
                    CopySource = {'Bucket':bucket_name, 'Key':object['Key']}
                )

                # Delete original object
                s3_client.delete_object(Bucket = bucket_name, Key = object['Key'])
                print(f"Deleted {object['Key']} from {bucket_name}")

                count += 1
    print(count, f"objects moved from bucket: {bucket_name}")

for bucket in buckets_list:
    iterate_s3_buckets(bucket)