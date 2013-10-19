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
        searchlist = ['name', ]
        list_app = [app, ]
        matches = yb.searchGenerator(searchlist, list_app)
        for (package, matched_value) in matches:
            if package.name == app:
                if type_transaction is 'Install':
                    yb.install(package)
                    yb.buildTransaction()
                    yb.processTransaction()
                elif type_transaction is 'Remove':
                    yb.remove(package)
                    yb.buildTransaction()
                return self.info(app)
