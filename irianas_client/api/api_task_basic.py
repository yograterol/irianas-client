# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
import os
import hashlib
import simplejson as json
from flask import request
from flask.ext.restful import Resource, abort
from irianas_client.system.basic_task_system import ShuttingSystem
from irianas_client.system.monitor_system import MonitorSystem
from irianas_client.decorators import require_token, path_file_token


class TaskBasicAPI(Resource):
    method_decorators = [require_token]

    def get(self, action):
        if action == 'shut':
            ShuttingSystem.shut_down()
        elif action == 'reboot':
            ShuttingSystem.reboot()
        elif action == 'suspend':
            ShuttingSystem.suspend()
        elif action == 'hibernate':
            ShuttingSystem.hibernate()
        elif action == 'monitor':
            monitor = dict(cpu=MonitorSystem.get_cpu_porcent(3),
                           memory=MonitorSystem.get_memory_used(True),
                           disk=MonitorSystem.get_disk_used(True))
            return monitor


class ConnectAPI(Resource):
    m = hashlib.sha512()

    def get(self):
        if request.form.get('ip') and request.form.get('token'):
            if os.path.exists(path_file_token):
                os.remove(path_file_token)
                if not os.path.exists(path_file_token):
                    return dict(logout='Ok')
                else:
                    return dict(logout='Not')
            else:
                return dict(logout='Not')

    def post(self):
        if request.form.get('ip'):
            ip = hashlib.sha512(request.form.get('ip')).hexdigest()

            if os.path.exists(path_file_token):
                if request.form.get('token'):
                    token = hashlib.sha512(request.form['token']).hexdigest()
                else:
                    return abort(401)

                file_token = open(path_file_token)
                tokens = json.loads(file_token.read())
                if tokens['token'] == token and tokens['ip'] == ip:
                    return dict(connected=1)
                else:
                    return dict(connected=0)
            else:
                token_rand = os.urandom(64).encode('hex')
                token = hashlib.sha512(token_rand).hexdigest()
                dict_token = dict(token=token, ip=ip)
                file_token = open(path_file_token, 'w')
                json.dump(dict_token, file_token)

                return dict(token=token_rand)
