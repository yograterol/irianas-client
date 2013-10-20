# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
from os import system


class ShuttingSystem(object):

    @staticmethod
    def shut_down():
        system("init 0")

    @staticmethod
    def reboot():
        system("reboot")

    @staticmethod
    def suspend():
        system("pm-suspend")

    @staticmethod
    def hibernate():
        system(" pm-hibernate")
