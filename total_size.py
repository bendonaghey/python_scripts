import boto3

bucket_name = 'display-portal-dev'
s3 = boto3.resource('s3')
bytes = sum([object.size for object in s3.Bucket(bucket_name).objects.all()])
print(f'total bucket size: {bytes//1000/1024/1024} GB')
print(f'total bucket size: {bytes//1000/1024} MBs')