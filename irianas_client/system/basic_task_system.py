# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
from os import system


class ShuttingSystem(object):

    def shut_down(self):
        system("init 0")

    def reboot(self):
        system("reboot")

    def suspend(self):
        system("pm-suspend")

    def hibernate(self):
        system(" pm-hibernate")
