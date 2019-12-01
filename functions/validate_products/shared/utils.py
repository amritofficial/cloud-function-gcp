import os

TEMPORARY_PATH='/tmp'


def create_temp_file_path(file_name):
    """
    Creates a tmp file path to dump the file in a read-only system
    :param file_name: the name of the file
    :return: tmp file path
    """

    path = os.path.join(TEMPORARY_PATH, file_name)

    return path
