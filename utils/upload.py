
from qiniu import Auth, put_file, etag
import qiniu.config

import os

from qiniu.services.storage.uploader import put_data


def uploadFile(file_name, file_path):

    access_key = os.environ.get('access_key')
    secret_key = os.environ.get('secret_key')
    print(access_key)
    print(secret_key)
    q = Auth(access_key, secret_key)
    bucket_name = "huahzongmysite"
    key = file_name
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = put_file(token, key, file_path=file_path)
    print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(data)
    return info, ret

if __name__ == '__main__':
    uploadFile('test','/home/python/github/mysite/aa.txt')