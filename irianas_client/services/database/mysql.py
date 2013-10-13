# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#

config_basic_ = {
    "mysqld":
    {
        "datadir": "/var/lib/mysql",
        "socket": "/var/lib/mysql/mysql.sock",
        "user": "mysql",
        "symbolic-links": 0},
    "mysqld_safe":
    {
        "log-error": "/var/log/mysqld.log",
        "pid-file": "/var/run/mysqld/mysqld.pid"
    }
}
