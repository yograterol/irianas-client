"""Test for MySQL Config Service.

.. moduleauthor:: Irisel Gonzalez <irisel.gonzalez@gmail.com>

"""
import pytest
from irianas_client.services.database import (MySQLService, MySQLConfigFile)

condition_test = "'VIRTUAL_ENV' in os.environ or 'TRAVIS' in os.environ"

obj_mysql = MySQLService()
obj_mysql_config_file = MySQLConfigFile()
tmp_path = '/tmp/my.cnf'
tmp_path_mysql_service = '/tmp/my_test.cnf'


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
        obj_mysql_config_file.save_file(tmp_path)
        assert open(tmp_path)

    def test_config_file_from_mysql_service(self):
        obj_mysql.save_attr(tmp_path_mysql_service)
        assert open(tmp_path_mysql_service)

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_install(self):
        assert obj_mysql.install()

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_uninstall(self):
        assert obj_mysql.remove()

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_reinstall(self):
        assert obj_mysql.install()

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_start_service(self):
        assert obj_mysql.start()

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_restart_service(self):
        assert obj_mysql.restart()

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_stop_service(self):
        assert obj_mysql.stop()
