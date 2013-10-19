# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
from irianas_client.config.config_services import CreateConfigFile
from irianas_client.services.commons import CommonService

"""
Config basic for BIND
"""

file_named_config = ("""
//
// named.conf
//
// Provided by Red Hat bind package to configure the ISC BIND named(8) DNS
// server as a caching only nameserver (as a localhost DNS resolver only).
//
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//

options {{
    listen-on port {port} {{ {ip_address}; }};
    listen-on-v6 port {port} {{ {ip_address_v6}; }};
    directory   "/var/named";
    dump-file   "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
    allow-query     {{ localhost; }};
    recursion yes;

    dnssec-enable yes;
    dnssec-validation yes;
    dnssec-lookaside auto;

    /* Path to ISC DLV key */
    bindkeys-file "/etc/named.iscdlv.key";

    managed-keys-directory "/var/named/dynamic";
}};

logging {{
        channel default_debug {{
                file "data/named.run";
                severity dynamic;
        }};
}};

zone "." IN {{
    type hint;
    file "named.ca";
}};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
""")

config_params = {
    "port": 53,
    "ip_address": '127.0.0.1',
    "ip_address_v6": '::1'
}


class BINDService(CommonService):
    """BIND Service"""

    def __init__(self):
        super(BINDService, self).__init__(config_params, 'bind')

    def save_attr(self, path):
        create_config = CreateConfigFile()
        create_config.save_file(file_named_config,
                                config_params,
                                path)

    def restart(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass
