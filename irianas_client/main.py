#!/usr/bin/env python
""":mod:`irianas_client.main` -- Program entry point
"""
import sys
sys.path[0:0] = [""]
from flask import Flask
from flask.ext import restful
from irianas_client.api.api_services import ApacheService


def main():
    app = Flask(__name__)
    api = restful.Api(app)
    api.add_resource(ApacheService, '/api/services/apache/<string:action>')

    app.run(debug=True)

if __name__ == '__main__':
    main()
