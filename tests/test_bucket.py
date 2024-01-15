import pytest
from checkers.aws import *


@pytest.mark.parametrize('create_and_clear_data', [{'file_name': 'file_for_test_upload.txt', 'file_key': 'test_file'}],
                         indirect=True)
def test_list_objects(request, set_api, create_and_clear_data):
    assert check_object_in_bucket(request.session.api.get_list_objects(request.session.bucket_name), 'test_file')
