# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
from flask import request
from irawadi_user import (UserExist, UserNotExist)
#from flask.ext.restful import fields
from irianas_client.config.config import ConfigIrianasClient
from irianas_client.services.webserver.apache import HTTPDService
from irianas_client.services.database.mysql import MySQLService
from irianas_client.services.ftp.vsftp import vsFTPService
from irianas_client.services.dns.bind import BINDService
from irianas_client.api.commons import APICommon

config_irianas = ConfigIrianasClient().config


class ApacheServiceAPI(APICommon):
    """

    """
    path = config_irianas['apache-service']['path_folder_config']

    def __init__(self):
        super(ApacheServiceAPI, self).__init__(HTTPDService(), 'httpd')

    def post(self):
        obj_httpd = HTTPDService()
        if request.form.get('domain'):
            result = obj_httpd.create_vhost(request.form.get('domain'),
                                            self.path)
            if result:
                return dict(vhost_status='Created')
            else:
                return dict(vhost_status='NotCreated')

    def put(self):
        pass

    def delete(self, action):
        obj_httpd = HTTPDService()
        if action:
            result = obj_httpd.remove_vhost(action,
                                            self.path)
            if result:
                return dict(vhost_status='Removed')
            else:
                return dict(vhost_status='NotRemoved')


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
    danger_users = ['root', 'apache', 'www', 'ftp', 'mysql', 'nologin',
                    'system', 'bin', 'sshd', 'named', 'lp', 'shutdown',
                    'sys', 'halt', 'mail', 'uucp', 'operators', 'nobody',
                    'rpc', 'dbus', 'gopher', 'avahi-autoipd', 'haldaemon',
                    'saslauth', 'postfix', 'pulse', 'ntp', 'gdm', 'rpcuser',
                    'nfsnobody', 'tcpdump', 'adm']

    def __init__(self):
        super(vsFTPServiceAPI, self).__init__(vsFTPService(), 'vsftpd')

    def post(self):
        obj_ftp = vsFTPService()
        try:
            if not request.form['user'] in self.danger_users:
                if obj_ftp.create_user(request.form['user'],
                                       request.form['password']):
                    return dict(result=1)
                else:
                    return dict(result=0)
            else:
                return dict(error='DangerUser')
        except UserExist:
            return dict(error='UserExist')

    def put(self):
        obj_ftp = vsFTPService()
        try:
            if not request.form['user'] in self.danger_users:
                if obj_ftp.update_password(request.form['user'],
                                           request.form['password']):
                    return dict(result=1)
                else:
                    return dict(result=0)
            else:
                return dict(error='DangerUser')
        except UserNotExist:
            return dict(error='UserNotExist')

    def delete(self, action):
        obj_ftp = vsFTPService()
        try:
            if not action in self.danger_users:
                if obj_ftp.remove_user(action):
                    return dict(result=1)
                else:
                    return dict(result=0)
            else:
                return dict(error='DangerUser')
        except UserNotExist:
            return dict(error='UserNotExist')
