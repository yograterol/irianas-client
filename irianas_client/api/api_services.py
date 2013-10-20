# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
#from flask import request
from flask.ext.restful import fields
from irianas_client.services.webserver.apache import (HTTPDService,
                                                      config_params)
from irianas_client.api.commons import APICommon


class ApacheService(APICommon):
    """

    """
    params_valid = dict(zip(config_params.keys(),
                            len(config_params.keys()) * [fields.Raw]))

    def __init__(self):
        super(ApacheService, self).__init__(HTTPDService(), 'httpd')

    def post(self, action):
        pass

    def put(self):
        pass
