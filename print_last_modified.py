import boto3
from datetime import datetime, timedelta
  
buckets_list = ['python-test-ben']
s3_client = boto3.client('s3')
days = 10

# Create a reusable Paginator
paginator = s3_client.get_paginator('list_objects_v2')

def iterate_s3_buckets(bucket_name):
    count = 0
    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket = bucket_name)

    # Loop through each object, looking for ones older than a given time period
    for page in page_iterator:  
        for object in page['Contents']:
            if object['LastModified'] < datetime.now().astimezone() - timedelta(days):
                print(f"{object['Key']}")

                count += 1
    print(count, f"new objects in bucket: '{bucket_name}' within the last {days} day/s")

for bucket in buckets_list:
    iterate_s3_buckets(bucket)