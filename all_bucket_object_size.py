# This script will get the total size in GBs of multiple buckets, add
# them together and display the result rounded to 5 decimal places

import boto3
from datetime import datetime, timedelta

from numpy import byte
  
buckets_list = ['display-portal-dev', 'cv-display-dev']

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
days = 1
bytes = 0
paginator = s3_client.get_paginator('list_objects_v2')

def iterate_s3_buckets(bucket_name):
    global bytes
    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket = bucket_name)

    # Loop through each object, looking for ones older than a given time period
    for page in page_iterator:  
        for object in page['Contents']:
            if object['LastModified'] < datetime.now().astimezone() - timedelta(days):
                bytes = sum([object.size for object in s3_resource.Bucket(bucket_name).objects.all()])

for bucket in buckets_list:
    bytes += bytes
    iterate_s3_buckets(bucket)

    
print(f'total bucket size: {round(bytes//1000/1024/1024, 5)} GB Total')
# print(f'total bucket size: {bytes//1000/1024} MBs')