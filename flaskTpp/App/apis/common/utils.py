import uuid

from App.settings import UPLOADS_DIR, FILE_PATH_PRIFIX


def filename_transfer(filename):
    ext_name=filename.rsplit('.')[1]
    new_filename=uuid.uuid4().hex
    filepath = UPLOADS_DIR + '/' + new_filename+'.'+ext_name
    bgpath = FILE_PATH_PRIFIX + '/' + new_filename+'.'+ext_name
    return filepath,bgpath

