from flask.ext import restful
from flask import request
from irianas_client.yumwrap.yumwrapper import YUMWrapper
from irianas_client.config.config import ConfigIrianasClient

config_irianas = ConfigIrianasClient().config


class APICommon(restful.Resource):
    __slots__ = ['services', 'obj_services']

    def __init__(self, obj_services, services):
        self.obj_services = obj_services
        self.services = services

    def get(self, action='status'):
        obj_yum = YUMWrapper()
        if action == 'installed':
            if obj_yum.info(self.services):
                return dict(status_service=1)
            return dict(status_service=0)
        elif action == 'install':
            if self.obj_services.install():
                self.obj_services.activate()
                return dict(status_service=1)
            return dict(status_service=0)
        elif action == 'remove':
            if self.obj_services.remove():
                self.obj_services.deactivate()
                return dict(status_service=1)
            return dict(status_service=0)
        elif action == 'start':
            self.obj_services.start()
        elif action == 'restart':
            self.obj_services.restart()
        elif action == 'stop':
            self.obj_services.stop()
        elif action == 'activate':
            self.obj_services.activate()
        elif action == 'deactivate':
            self.obj_services.deactivate()

        status = dict()
        if self.obj_services.get_status():
            status['status'] = 1
        else:
            status['status'] = 0
        return status


class APIConfigCommmon(restful.Resource):

    __slots__ = ['services', 'obj_services']

    def __init__(self, obj_services, services):
        self.obj_services = obj_services
        self.services = services

    def get(self):
        return self.obj_services.get_dict_params()

    def put(self):
        if request.form:
            for key, value in request.form.iteritems():
                self.obj_services.set(key, value)
            path = config_irianas[self.services]['path_config_file']
            self.obj_services.save_attr(path)
            self.obj_services.restart()
            return dict(result=1)
        else:
            return dict(result=0)
