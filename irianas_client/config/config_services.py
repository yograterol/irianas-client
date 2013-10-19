"""
.. module:: config_services
   :platform: Linux
   :synopsis: Services Config module, create the file config with the
              string configs and params.

.. moduleauthor:: Irisel Gonzalez <irisel.gonzalez@gmail.com>


"""


class CreateConfigFile(object):

    def __init__(self):
        super(CreateConfigFile, self).__init__()

    def create_config_string(self, string_config, params):
        return string_config.format(**params)

    def save_file(self, string_config, params, path):
        config_file = open(path, 'w')
        config_file.write(self.create_config_string(string_config, params))
        config_file.close()
