# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
from ctrldaemon import ControlDaemon
from irianas_client.config.config import ConfigIrianasClient
try:
    from irianas_client.yumwrap.yumwrapper import YUMWrapper
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

    def install(self, package=None):
        yum = YUMWrapper()
        if not package:
            return yum.transaction(self.app['name_package'])
        return yum.transaction(package)

    def remove(self, package=None):
        yum = YUMWrapper()
        if not package:
            return yum.transaction(self.app['name_package'], 'Remove')
        return yum.transaction(package)

    def start(self):
        return self._exec_command_service('start')

    def restart(self):
        return self._exec_command_service('restart')

    def stop(self):
        return self._exec_command_service('stop')

    def get_status(self):
        return self._exec_command_service('get_status')

    def activate(self):
        return self._exec_command_service('activate')

    def deactivate(self):
        return self._exec_command_service('deactivate')

    def _exec_command_service(self, command):
        obj_daemon = ControlDaemon(self.app['service_name'])
        actions = dict(start=obj_daemon.start,
                       restart=obj_daemon.restart,
                       stop=obj_daemon.stop,
                       get_status=obj_daemon.get_status,
                       activate=obj_daemon.activate,
                       deactivate=obj_daemon.deactivate)
        return actions[command]()
