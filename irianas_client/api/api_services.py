# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
from flask.ext import restful
from irianas_client.services.webserver.apache import HTTPDService


class ApacheService(restful.Resource):
    """

    """
    obj_apache = HTTPDService()

    def get(self):
        status = dict()
        if self.obj_apache.get_status():
            status['status'] = 1
        else:
            status['status'] = 0
        return status
