import os
import hashlib
import simplejson as json
from flask import request
from flask.ext.restful import abort

path_file_token = os.path.join('/etc/', 'irianas_token.tk')


def require_token(f):
    def inner(*args, **kwargs):
        if os.path.exists(path_file_token):
            file_token = open(path_file_token)
            data_json = json.loads(file_token.read())

            token = hashlib.sha512(request.form.get('token')).hexdigest()
            ip = hashlib.sha512(request.form.get('ip')).hexdigest()

            if data_json.get('token') == token and data_json.get('ip') == ip:
                return f(*args, **kwargs)
            else:
                return abort(401)
        else:
            return abort(401)
    return inner
