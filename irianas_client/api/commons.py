from flask.ext import restful
from irianas_client.yumwrap.yumwrapper import YUMWrapper


class APICommon(restful.Resource):
    __slots__ = ['services', 'obj_services']

    def __init__(self, obj_services, services):
        self.obj_services = obj_services
        self.services = services

    def get(self, action='status'):
        obj_yum = YUMWrapper()
        if action == 'installed':
            return dict(installed=obj_yum.info(self.services))
        elif action == 'install':
            return dict(installed=self.obj_services.install())
        elif action == 'remove':
            return dict(remove=not self.obj_services.remove())
        elif action == 'start':
            self.obj_services.start()
        elif action == 'restart':
            self.obj_services.restart()
        elif action == 'stop':
            self.obj_services.stop()

        status = dict()
        if self.obj_services.get_status():
            status['status'] = 1
        else:
            status['status'] = 0
        return status
