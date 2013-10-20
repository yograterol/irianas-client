"""Test for Config Class.

.. moduleauthor:: Irisel Gonzalez <irisel.gonzalez@gmail.com>

"""
from irianas_client.config import ConfigIrianasClient


def create_config():
    """Create the Config object."""
    return ConfigIrianasClient().config


class TestConfig(object):

    def test_config(self):
        config = create_config()
        assert config

    def test_config_mysql(self):
        config = create_config()
        assert 'mysql-service' in config
        assert config['mysql-service'].get('service_name') == 'mysqld'
