# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#

config_basic = ("""[mysqld]
datadir={0}
socket={1}
user={2}
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links={3}

[mysqld_safe]
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid""")
