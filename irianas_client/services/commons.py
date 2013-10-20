from ctrldaemon import ControlDaemon
from irianas_client.config.config import ConfigIrianasClient
try:
    from irianas_client.yum.yumwrapper import YUMWrapper
except:
    YUMWrapper = None
config_irianas = ConfigIrianasClient()


class CommonService(object):
    __slots__ = ['config_params', 'app']

    def __init__(self, config_params, name_service):
        self.config_params = config_params
        self.app = config_irianas.config[name_service + '-service']

    def __getattr__(self, attr):
        if attr in self.config_params:
            return self.config_params[attr]

    def __setattr__(self, attr, value):
        if not attr is 'config_params' and not attr is 'app':
            if attr in self.config_params:
                self.config_params[attr] = value
        else:
            object.__setattr__(self, attr, value)

    def get(self, attr):
        return self.__getattr__(attr)

    def set(self, attr, value):
        self.__setattr__(attr, value)

    def install(self):
        yum = YUMWrapper()
        return yum.transaction(self.app['name_package'])

    def remove(self):
        yum = YUMWrapper()
        return yum.transaction(self.app['name_package'], 'Remove')

    def start(self):
        return self._exec_command_service('start')

    def restart(self):
        return self._exec_command_service('restart')

    def stop(self):
        return self._exec_command_service('stop')

    def get_status(self):
        return self._exec_command_service('get_status')

    def _exec_command_service(self, command):
        obj_daemon = ControlDaemon(self.app['service_name'])
        actions = dict(start=obj_daemon.start,
                       restart=obj_daemon.restart,
                       stop=obj_daemon.stop,
                       get_status=obj_daemon.get_status)
        return actions[command]()
