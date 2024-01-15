import random
from pathlib import Path
import os
import pytest

from lib.api import Api


@pytest.fixture(scope='session')
def set_api(request):
    request.session.api = Api()


@pytest.fixture(scope='function')
def generate_bucket_name(request):
    request.session.bucket_name = ''.join(['antonov-test-bucket', str(random.randint(1, 100))])


@pytest.fixture(scope='function')
def create_and_clear_data(request, set_api, generate_bucket_name):
    request.session.api.put_bucket(name=request.session.bucket_name)
    request.session.api.upload_object(bucket_name=request.session.bucket_name,
                                      file_name=os.path.join(Path(__file__).parent.parent, 'test_data',
                                                             request.param['file_name']),
                                      file_key=request.param['file_key'])
    yield
    request.session.api.delete_object(bucket_name=request.session.bucket_name, file_key=request.param['file_key'])
    request.session.api.delete_bucket(name=request.session.bucket_name)
