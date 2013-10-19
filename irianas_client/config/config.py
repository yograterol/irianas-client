"""
.. module:: config
   :platform: Linux
   :synopsis: Config module.

.. moduleauthor:: Irisel Gonzalez <irisel.gonzalez@gmail.com>


"""
import os
from yaml import load


class ConfigIrianasClient(object):
    """ConfigIrianasClient"""
    path_config_file = '/etc/irianas_config.conf'

    def __init__(self):
        super(ConfigIrianasClient, self).__init__()
        if 'VIRTUAL_ENV' in os.environ:
            self.path_config_file = os.path.join(os.environ['VIRTUAL_ENV'],
                                                 'irianas_config.conf')

        self.load_config()

    def load_config(self):
        """This method load the config file in YAML syntax."""
        config_file = open(self.path_config_file)
        self.config = load(config_file)
        config_file.close()
