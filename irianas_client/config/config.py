"""
.. module:: config
   :platform: Linux
   :synopsis: Config module.

.. moduleauthor:: Irisel Gonzalez <irisel.gonzalez@gmail.com>


"""
from yaml import load


class ConfigIrianasClient(object):
    """ConfigIrianasClient"""
    path_config_file = '/etc/irianas_config.conf'

    def __init__(self, test=False):
        super(ConfigIrianasClient, self).__init__()
        if not test:
            self.load_config()
        else:
            config = ("""mysql-service:
                      name_package: mysql-server
                      path_config_file: /etc/my.cnf""")
            self.config = load(config)

    def load_config(self):
        """This method load the config file in YAML syntax."""
        config_file = open(self.path_config_file)
        self.config = load(config_file)
        config_file.close()
