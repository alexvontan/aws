import boto3
import os
import logging


class Api:
    def __init__(self):
        host = ''.join(['http://', os.getenv('aws_host')])
        self.client = boto3.client('s3', endpoint_url=host)
        self.s3 = boto3.resource('s3', endpoint_url=host)

    def get_buckets(self):
        return self.s3.buckets.all()

    def get_bucket_by_name(self, name=None):
        if self.s3.Bucket(name).creation_date:
            return True
        else:
            return False

    def put_bucket(self, name=None):
        self.client.create_bucket(Bucket=name)
        logging.info(f'Создан bucket {name}')

    def delete_bucket(self, name):
        self.client.delete_bucket(Bucket=name)
        logging.info(f'Удален bucket {name}')

    def upload_object(self, bucket_name=None, file_name=None, file_key=None):
        self.client.put_object(Bucket=bucket_name, Key=file_key, Body=file_name)
        logging.info(f'Добавлен объект {file_key} в bucket {bucket_name}')

    def delete_object(self, bucket_name=None, file_key=None):
        self.client.delete_object(Bucket=bucket_name, Key=file_key)
        logging.info(f'Удален объект {file_key} из bucket {bucket_name}')

    def get_list_objects(self, bucket_name=None):
        return self.client.list_objects_v2(Bucket=bucket_name)
