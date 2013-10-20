# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
import yum
import os


class YUMWrapper(object):

    def info(self, app):
        yb = yum.YumBase()
        if yb.rpmdb.searchNevra(name=app):
            return True
        else:
            return False

    def transaction(self, app, type_transaction='Install'):
        if type_transaction == 'Install':
            os.system("yum install -y " + app)
        elif type_transaction == 'Remove':
            os.system("yum remove -y " + app)
        elif type_transaction == 'Update':
            os.system("yum update -y" + app)
        return self.info(app)
