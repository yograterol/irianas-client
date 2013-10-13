"""Test for MySQL Config Service.

.. moduleauthor:: Irisel Gonzalez <irisel.gonzalez@gmail.com>

"""
from irianas_client.services.database import (MySQLService, MySQLConfigFile)

obj_mysql = MySQLService()
obj_mysql_config_file = MySQLConfigFile()


class TestMySQLService(object):

    def test_params(self):
        assert obj_mysql.get('bind-address') == '0.0.0.0'

    def test_set_params(self):
        obj_mysql.set('bind-address', '1.1.1.1')
        assert obj_mysql.get('bind-address') == '1.1.1.1'

    def test_config_file(self):
        assert obj_mysql_config_file.config == dict()

    def test_config_file_concat(self):
        obj_mysql_config_file.concat_params_mysqld()
        obj_mysql_config_file.add_params_mysqld_safe()
        assert obj_mysql_config_file.config != dict()

    def test_config_file_string(self):
        obj_mysql_config_file.create_config_string()
        assert '[mysqld]' in obj_mysql_config_file.config_string
        assert '[mysqld_safe]' in obj_mysql_config_file.config_string

    def test_config_file_save(self):
        tmp_path = '/tmp/my.cnf'
        obj_mysql_config_file.save_file(tmp_path)
        assert open(tmp_path)
