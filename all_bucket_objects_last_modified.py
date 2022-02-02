# This script will list the total objects from 1 or more buckets passed 
# into the script and print the total

import boto3
from datetime import datetime, timedelta
  
buckets_list = ['']
s3_client = boto3.client('s3')
days = 1
count = 0
paginator = s3_client.get_paginator('list_objects_v2')

def iterate_s3_buckets(bucket_name):
    global count
    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket = bucket_name)

    # Loop through each object, looking for ones older than a given time period
    for page in page_iterator:  
        for object in page['Contents']:
            if object['LastModified'] < datetime.now().astimezone() - timedelta(days):
                count += 1

for bucket in buckets_list:
    iterate_s3_buckets(bucket)

print(count, f"new objects within last {days} days")