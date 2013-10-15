import yum


class YUMWrapper(object):

    def info(self, app):
        yb = yum.YumBase()
        if yb.rpmdb.searchNevra(name=app):
            return True
        else:
            return False

    def install(self, app):
        yb = yum.YumBase()
        searchlist = [app, ]
        arg = [app, ]
        matches = yb.searchGenerator(searchlist, arg)
        for (package, matched_value) in matches:
            if package.name == app:
                print yb.install(package)
                print yb.buildTransaction()
                print yb.processTransaction()
