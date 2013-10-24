import os
import hashlib
import simplejson as json
from flask import request
from flaks.ext.restful import abort
from irianas_clent.api import path_file_token


def require_token(f):
    def inner(*args, **kwargs):
        if os.path.exists(path_file_token):
            file_token = open(path_file_token)
            data_json = json.loads(file_token)

            token = hashlib.sha512(request.form.data['token']).hexdigest()
            ip = hashlib.sha512(request.form.data['ip']).hexdigest()

            if data_json.get('token') == token and \
               data_json.get('ip') == ip:
                return f(*args, **kwargs)
            else:
                return abort(401)
        else:
            return abort(401)
    return inner
