from flask.ext import restful
from irianas_client.yumwrap.yumwrapper import YUMWrapper


class APICommon(restful.Resource):
    __slots__ = ['services', 'obj_services']

    def __init__(self, obj_services, services):
        self.obj_services = obj_services
        self.services = services

    def get(self, action):
        obj_yum = YUMWrapper()
        if action == 'status':
            status = dict()
            if self.obj_services.get_status():
                status['status'] = 1
            else:
                status['status'] = 0
            return status
        elif action == 'installed':
            return dict(installed=obj_yum.info(self.services))
        elif action == 'install':
            return dict(installed=obj_yum.transaction(self.services))
        elif action == 'remove':
            return dict(service=self.services,
                        remove=obj_yum.transaction(self.services, 'Remove'))
