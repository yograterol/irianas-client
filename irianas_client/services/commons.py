

class CommonService(object):
    __slots__ = ['config_params', ]

    def __init__(self, config_params):
        self.config_params = config_params

    def __getattr__(self, attr):
        if not attr is 'config_params':
            if attr in self.config_params:
                return self.config_params[attr]
            else:
                return None

    def __setattr__(self, attr, value):
        if not attr is 'config_params':
            if attr in self.config_params:
                self.config_params[attr] = value
        else:
            object.__setattr__(self, attr, value)

    def get(self, attr):
        return self.__getattr__(attr)

    def set(self, attr, value):
        self.__setattr__(attr, value)
