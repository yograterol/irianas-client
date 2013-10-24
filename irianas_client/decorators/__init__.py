import os
import hashlib
import simplejson as json
from flask import request
from flask.ext.restful import abort

path_file_token = os.path.join('/etc/', 'irianas_token.tk')


def require_token(f):
    def inner(*args, **kwargs):
        print "In the decorator"
        if os.path.exists(path_file_token):
            print "Exist the file"
            file_token = open(path_file_token)
            print "File opened"
            data_json = json.loads(file_token.read())
            print "File open"

            token = hashlib.sha512(request.form.get('token')).hexdigest()
            ip = hashlib.sha512(request.form.get('ip')).hexdigest()

            if data_json.get('token') == token and data_json.get('ip') == ip:
                return f(*args, **kwargs)
            else:
                return abort(401)
        else:
            return abort(401)
    return inner
