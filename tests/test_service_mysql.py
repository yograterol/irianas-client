"""Test for MySQL Config Service.

.. moduleauthor:: Irisel Gonzalez <irisel.gonzalez@gmail.com>

"""
from irianas_client.services.database import MySQLService

obj_mysql = MySQLService()


class TestMySQLService(object):

    def test_params(self):
        assert obj_mysql.get('bind-address') == '0.0.0.0'

    def test_set_params(self):
        obj_mysql.set('bind-address', '1.1.1.1')
        assert obj_mysql.get('bind-address') == '1.1.1.1'
