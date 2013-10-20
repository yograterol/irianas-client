# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
#from flask import request
#from flask.ext.restful import fields
from irianas_client.services.webserver.apache import HTTPDService
from irianas_client.services.database.mysql import MySQLService
from irianas_client.services.ftp.vsftp import vsFTPService
from irianas_client.services.dns.bind import BINDService

from irianas_client.api.commons import APICommon


class ApacheServiceAPI(APICommon):
    """

    """

    def __init__(self):
        super(ApacheServiceAPI, self).__init__(HTTPDService(), 'httpd')

    def post(self, action):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class MySQLServiceAPI(APICommon):
    """

    """

    def __init__(self):
        super(MySQLServiceAPI, self).__init__(MySQLService(), 'mysql-server')

    def post(self, action):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class BINDServiceAPI(APICommon):
    """

    """

    def __init__(self):
        super(BINDServiceAPI, self).__init__(BINDService(), 'bind')

    def post(self, action):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class vsFTPServiceAPI(APICommon):
    """

    """

    def __init__(self):
        super(vsFTPServiceAPI, self).__init__(vsFTPService(), 'vsftpd')

    def post(self, action):
        pass

    def put(self):
        pass

    def delete(self):
        pass
