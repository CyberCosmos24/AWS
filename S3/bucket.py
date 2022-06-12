from secrets import access_key, secret_access_key
import click
import boto3



client =  boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

@click.group()
def cli():
    pass

@click.command()
def list_bucket():
    list = client.list_buckets()
    if list:
        print('Buckets exists..')
        for bucket in list['Buckets']:
            print(f'  {bucket["Name"]}')
@click.command()
def make_bucket():
    create = input("Do you want to create a bucket? Yes or No: ")
    if create == "yes":
        Bucket_value = input("Enter bucket name: ")
        region_value = input("Enter region name: ")
        client.create_bucket(Bucket = Bucket_value, Region = region_value)
    elif create == "no":
        return 
@click.command() 
def delete_bucket():
    delete = input("Do you want to delete a bucket? Yes or No: ")
    if delete == "yes":
        Bucket_value = input("Enter bucket name: ")
        client.delete_bucket(Bucket = Bucket_value)
    elif delete == "no":
        return 0
    
    
    
cli.add_command(list_bucket)
cli.add_command(make_bucket)
cli.add_command(delete_bucket)

if __name__ == '__main__':
    cli()
  