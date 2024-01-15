def check_object_in_bucket(list_objects=None, object_name=None):
    for obj in list_objects['Contents']:
        if obj['Key'] == object_name:
            return True
    return False
