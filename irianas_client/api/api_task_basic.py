# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
from flask.ext.restful import Resource
from irianas_client.system.basic_task_system import ShuttingSystem


class TaskBasicAPI(Resource):

    def get(self, action):
        if action == 'shut':
            ShuttingSystem.shut_down()
        elif action == 'reboot':
            ShuttingSystem.reboot()
        elif action == 'suspend':
            ShuttingSystem.suspend()
        elif action == 'hibernate':
            ShuttingSystem.hibernate()
