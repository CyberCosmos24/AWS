from secrets import access_key, secret_access_key

import boto3
import os 
upload_file_bucket = input("Enter the S3 bucket you want to use: ") 
"""
You do need a AWS S3 bucket in order to use this.

"""
upload_file_key = input("Set a file key: ")
"""
Example: 'Folder/'

"""
client =  boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
for file in os.listdir():
    if '.py' in file: # You can change what file type you want.
        client.upload_file(file, upload_file_bucket, upload_file_key)
        print("Files uploaded successfully")
    
