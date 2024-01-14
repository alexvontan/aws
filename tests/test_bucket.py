import pytest


@pytest.mark.parametrize('create_and_clear_data', [{'file_name': 'file_for_test_upload.txt', 'file_key': 'test_file'}],
                         indirect=True)
def test_list_objects(request, set_api, create_and_clear_data):
    assert request.session.api.get_bucket_by_name(request.session.bucket_name)
    assert request.session.api.get_list_objects(request.session.bucket_name)['KeyCount'] == 1
