#!/usr/bin/env python
""":mod:`irianas_client.main` -- Program entry point
"""
import sys
sys.path[0:0] = [""]
from flask import Flask
from flask.ext import restful
from irianas_client.api.api_services import \
    (ApacheServiceAPI, MySQLServiceAPI, vsFTPServiceAPI, BINDServiceAPI)
from irianas_client.api.api_task_basic import TaskBasicAPI

api_services = '/api/services/'
api_task = '/api/task/'


def main():
    app = Flask(__name__)
    api = restful.Api(app)
    api.add_resource(ApacheServiceAPI, api_services + 'apache/<string:action>',
                     api_services + 'apache')
    api.add_resource(MySQLServiceAPI, api_services + 'mysql/<string:action>',
                     api_services + 'mysql')
    api.add_resource(vsFTPServiceAPI, api_services + 'vsftpd/<string:action>',
                     api_services + 'vsftpd')
    api.add_resource(BINDServiceAPI, api_services + 'bind/<string:action>',
                     api_services + 'bind')

    api.add_resource(TaskBasicAPI, api_task + '<string:action>')

    app.run(debug=True)

if __name__ == '__main__':
    main()
