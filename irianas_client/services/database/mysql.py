# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#

"""
Config basic for the config file my.cnf
"""
config_basic = {
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

params_valid = ["bind-address", "binlog_cache_size", "bulk_insert_buffer_size",
                "connect_timeout", "completion_type", "concurrent_insert",
                "innodb_additional_mem_pool_size",
                "innodb_autoextend_increment",
                "innodb_buffer_pool_awe_mem_mb", "innodb_buffer_pool_size",
                "innodb_checksums", "innodb_commit_concurrency",
                "innodb_concurrency_tickets", "innodb_data_file_path",
                "innodb_fast_shutdown", "innodb_file_io_threads",
                "innodb_file_per_table", "innodb_flush_log_at_trx_commit",
                "innodb_force_recovery", "innodb_lock_wait_timeout",
                "innodb_locks_unsafe_for_binlog", "join_buffer_size",
                "interactive_timeout", "keep_files_on_create",
                "key_buffer_size", "key_cache_age_threshold",
                "key_cache_block_size", "key_cache_division_limit",
                "max_allowed_packet", "max_connections",
                "max_delayed_threads", "max_join_size",
                "max_sort_length", "max_sp_recursion_depth",
                "query_cache_limit", "query_cache_min_res_unit",
                "query_cache_size", "query_cache_type", "socket",
                "sort_buffer_size", "wait_timeout"]

params_default = {
    "mysqld":
    {
        "bind-address": "0.0.0.0",
        "binlog_cache_size": 32768,
        "bulk_insert_buffer_size": 8388608,
        "connect_timeout": 10,
        "completion_type": 0,
        "concurrent_insert": True,
        "innodb_additional_mem_pool_size": 1048576,
        "innodb_autoextend_increment": 8,
        "innodb_buffer_pool_awe_mem_mb": 0,
        "innodb_buffer_pool_size": 8388608,
        "innodb_checksums": True,
        "innodb_commit_concurrency": 0,
        "innodb_concurrency_tickets": 500,
        "innodb_data_file_path": "ibdata1:10M:autoextend",
        "innodb_fast_shutdown": 1,
        "innodb_file_io_threads": 4,
        "innodb_file_per_table": False,
        "innodb_flush_log_at_trx_commit": 1,
        "innodb_force_recovery": 0,
        "innodb_lock_wait_timeout": 50,
        "innodb_locks_unsafe_for_binlog": False,
        "join_buffer_size": 131072,
        "interactive_timeout": 28800,
        "keep_files_on_create": False,
        "key_buffer_size": 8388608,
        "key_cache_age_threshold": 300,
        "key_cache_block_size": 1024,
        "key_cache_division_limit": 100,
        "max_allowed_packet": 1048576,
        "max_connections": 100,
        "max_delayed_threads": 20,
        "max_join_size": 4294967295,
        "max_sort_length": 1024,
        "max_sp_recursion_depth": 0,
        "query_cache_limit": 1048576,
        "query_cache_min_res_unit": 4096,
        "query_cache_size": 0,
        "query_cache_type": 1,
        "socket": "/tmp/mysql.sock",
        "sort_buffer_size": 2097144,
        "wait_timeout": 28800
    }
}


class MySQLConfigFile(object):
    """MySQLConfigFile"""
    config = dict()
    config_string = ""

    def __init__(self):
        super(MySQLConfigFile, self).__init__()

    def concat_params_mysqld(self):
        self.config["mysqld"] = dict(config_basic["mysqld"].items() +
                                     params_default["mysqld"].items())

    def add_params_mysqld_safe(self):
        self.config["mysqld_safe"] = config_basic["mysqld_safe"]

    def create_config_string(self):
        for key_mysql, value_mysql in self.config.iteritems():
            self.config_string += "[{0}]\n".format(key_mysql)
            for key, value in value_mysql.iteritems():
                self.config_string += "{0} = {1}\n".format(key, value)
            self.config_string += "\n\n"

    def save_file(self, path):
        config_file = open(path, 'w')
        config_file.write(self.config_string)
        config_file.close()

    def execute_config(self, path):
        self.concat_params_mysqld()
        self.add_params_mysqld_safe()
        self.create_config_string()
        self.save_file(path)


class MySQLService(object):
    """MySQLService"""

    def __init__(self):
        super(MySQLService, self).__init__()

    def __getattr__(self, attr):
        if attr in params_valid:
            return params_default["mysqld"][attr]
        else:
            return None

    def __setattr__(self, attr, value):
        if attr in params_valid:
            params_default["mysqld"][attr] = value

    def get(self, attr):
        return self.__getattr__(attr)

    def set(self, attr, value):
        self.__setattr__(attr, value)

    def save_attr(self, path):
        obj_mysql_config_file = MySQLConfigFile()
        obj_mysql_config_file.execute_config(path)

    def get_attr(self):
        pass

    def restart(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass
