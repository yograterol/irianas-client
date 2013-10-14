# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#

"""
Config basic for the config file httpd.conf
"""

module_active = ["modules/mod_auth_basic.so", "modules/mod_auth_digest.so",
                 "modules/mod_authn_file.so", "modules/mod_authn_alias.so",
                 "modules/mod_authn_anon.so", "modules/mod_authn_dbm.so",
                 "modules/mod_authn_default.so", "modules/mod_authz_host.so",
                 "modules/mod_authz_user.so", "modules/mod_authz_owner.so",
                 "modules/mod_authz_groupfile.so", "modules/mod_authz_dbm.so",
                 "modules/mod_authz_default.so", "modules/mod_ldap.so",
                 "modules/mod_authnz_ldap.so", "modules/mod_include.so",
                 "modules/mod_log_config.so", "modules/mod_logio.so",
                 "modules/mod_env.so", "modules/mod_ext_filter.so",
                 "modules/mod_mime_magic.so", "modules/mod_expires.so",
                 "modules/mod_deflate.so", "modules/mod_headers.so",
                 "modules/mod_usertrack.so", "modules/mod_setenvif.so",
                 "modules/mod_mime.so", "modules/mod_status.so",
                 "modules/mod_autoindex.so", "modules/mod_info.so",
                 "modules/mod_dav_fs.so", "modules/mod_vhost_alias.so",
                 "modules/mod_negotiation.so", "modules/mod_dir.so",
                 "modules/mod_actions.so", "modules/mod_speling.so",
                 "modules/mod_userdir.so", "modules/mod_substitute.so",
                 "modules/mod_rewrite.so", "modules/mod_proxy.so",
                 "modules/mod_proxy_balancer.so", "modules/mod_proxy_ftp.so",
                 "modules/mod_proxy_http.so", "modules/mod_proxy_ajp.so",
                 "modules/mod_proxy_connect.so", "modules/mod_cache.so",
                 "modules/mod_suexec.so", "modules/mod_disk_cache.so",
                 "modules/mod_cgi.so", "modules/mod_version.so"]

module_inactive = ["modules/mod_asis.so", "modules/mod_authn_dbd.so",
                   "modules/mod_cern_meta.so", "modules/mod_cgid.so",
                   "modules/mod_dbd.so", "modules/mod_filter.so",
                   "modules/mod_ident.so", "modules/mod_log_forensic.so"
                   "modules/mod_unique_id.so"]

params_default = {
    "apache":
    {
        "ServerTokens": "OS",
        "ServerRoot": "/etc/httpd",
        "PidFile": "run/httpd.pid",
        "Timeout": 60,
        "KeepAlive": False,
        "MaxKeepAliveRequests": 100,
        "KeepAliveTimeout": 15,
        "Listen": 80,
        "ExtendedStatus": True,
        "User": "apache",
        "Group": "apache",
        "ServerAdmin": "root@localhost",
        "ServerName": "localhost:80",
        "UseCanonicalName": False
        "DocumentRoot": "/var/www/html",
        "AllowOverride": None,
        "Options": ["Indexes", "FollowSymLinks"],
        "Order": ["allow", "deny"],
        "Allow": "from all",
        "DirectoryIndex": ["index.html", "index.html.var"],
        "AccessFileName": ".htaccess",
        "TypesConfig": "/etc/mime.types",
        "DefaultType": "text/plain",
    },
    "prefork":
    {
        "StartServers": 8,
        "MinSpareServers": 5,
        "MaxSpareServers": 20,
        "ServerLimit": 256,
        "MaxClients": 256,
        "MaxRequestsPerChild": 4000
    },
    "worker":
    {
        "StartServers": 4,
        "MaxClients": 300,
        "MinSpareThreads": 25,
        "MaxSpareThreads": 75,
        "ThreadsPerChild": 25,
        "MaxRequestsPerChild": 0
    },
    "Directory":
    {
        "/":
        {
            "Options": "FollowSymLinks",
            "AllowOverride": None
        }
    }
}


class HTTPDConfigFile(object):
    """HTTPDConfigFile"""
    config_string = ""

    def __init__(self):
        super(HTTPDConfigFile, self).__init__()

    def create_config_string(self):
        for key_httpd, value_httpd in self.config.iteritems():
            for key, value in value_httpd.iteritems():
                self.config_string += "{0} = {1}\n".format(key, value)
            self.config_string += "\n\n"

    def save_file(self, path):
        config_file = open(path, 'w')
        config_file.write(self.config_string)
        config_file.close()

    def execute_config(self, path):
        self.create_config_string()
        self.save_file(path)


class HTTPDService(object):
    """HTTPDService"""

    def __init__(self):
        super(HTTPDService, self).__init__()

    def __getattr__(self, attr):
        if attr in:
            return params_default[attr]
        else:
            return None

    def __setattr__(self, attr, value):
        if attr in:
            params_default[""][attr] = value

    def get(self, attr):
        return self.__getattr__(attr)

    def set(self, attr, value):
        self.__setattr__(attr, value)

    def save_attr(self, path):
        obj_httpd_config_file = HTTPDConfigFile()
        obj_httpd_config_file.execute_config(path)

    def get_attr(self):
        pass

    def restart(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass
