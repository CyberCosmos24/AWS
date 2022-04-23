from secrets import access_key, secret_access_key

import boto3
import os 


client =  boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
print(access_key)
print(secret_access_key)
create = input("Do you want to create a bucket? Yes or No: ")
if create == "yes":
    Bucket_value = input("Enter bucket name: ")
    region_value = input("Enter region name: ")
    client.create_bucket(Bucket = Bucket_value, Region = region_value)
elif create == "no":
    response = client.list_buckets()
    if response:
        print('Buckets exists..')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

    bucket = input("Enter the S3 bucket you want to use: ") 

