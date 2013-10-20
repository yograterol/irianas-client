# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
import yum


class YUMWrapper(object):

    def info(self, app):
        yb = yum.YumBase()
        if yb.rpmdb.searchNevra(name=app):
            return True
        else:
            return False

    def transaction(self, app, type_transaction='Install'):
        yb = yum.YumBase()
        yb.doConfigSetup()
        yb.doTsSetup()
        yb.doRpmDBSetup()
        yb.conf

        searchlist = ['name', ]
        list_app = [app, ]
        matches = yb.searchGenerator(searchlist, list_app)
        for (package, matched_value) in matches:
            if type_transaction is 'Install':
                yb.install(package)
                yb.buildTransaction()
                yb.resolveDeps()
                yb.processTransaction()
            elif type_transaction is 'Remove':
                yb.remove(name=package.name)
                yb.resolveDeps()
                yb.processTransaction()
            return self.info(app)

    def upgrade(refresh=True):
        '''
        Run a full system upgrade, a yum upgrade
        '''
        yb = yum.YumBase()

        try:
            yb.update()
            yb.resolveDeps()
            yb.closeRpmDB()
        except:
            pass
