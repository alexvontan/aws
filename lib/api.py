import boto3
import os


class Api:
    def __init__(self):
        access_key = os.getenv('aws_access_key')
        secret_key = os.getenv('aws_secret_key')
        host = ''.join(['http://', os.getenv('aws_host')])
        self.client = boto3.client('s3', region_name='ru-msk', endpoint_url=host, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        self.s3 = boto3.resource('s3', endpoint_url=host, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    def get_buckets(self):
        return self.s3.buckets.all()

    def get_bucket_by_name(self, name):
        if self.s3.Bucket(name).creation_date:
            return True
        else:
            return False

    def put_bucket(self, name):
        self.client.create_bucket(Bucket=name)

    def delete_bucket(self, name):
        self.client.delete_bucket(Bucket=name)

    def upload_object(self, bucket_name=None, file_name=None, file_key=None):
        # self.s3.Object(bucket_name, file_key).upload_file(file_name)
        self.client.put_object(Bucket=bucket_name, Key=file_key, Body=file_name)

    def delete_object(self, bucket_name, file_key):
        self.client.delete_object(Bucket=bucket_name, Key=file_key)

    def get_list_objects(self, bucket_name):
        return self.client.list_objects_v2(Bucket=bucket_name)
