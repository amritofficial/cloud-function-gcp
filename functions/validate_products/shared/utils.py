import os

TEMPORARY_PATH='/tmp'


def create_temp_file_path(file_name):
    path = os.path.join(TEMPORARY_PATH, file_name)

    return path
