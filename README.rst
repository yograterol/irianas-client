.. |master| image:: https://secure.travis-ci.org/Irigonzalez/irianas-client.png?branch=master
   :alt: Build Status - master branch
   :target: http://travis-ci.org/#!/Irigonzalez/irianas-client

================
Irianas (Client)
================

:Info: Irianas is a software for manage servers and clusters.
:Repository: https://github.com/Irigonzalez/irianas-client
:Authors: Irisel Gonzalez (http://github.com/irigonzalez) | Yohan Graterol (http://github.com/yograterol)
:IRC: #irianas (Freenode)
:Branch Master: |master|

Installation
============

    # python setup.py install

Test
====

    # paver run_test

Task List
=========

- [x] Yum wrapper
- [x] Config file and Config Class (+ Test)
- [x] Methods for the service's configuration (+ Test)
- [ ] Creation Client with Twisted for Connect to Irianas Server (+ Test)
- [ ] Creation reader for service's log. (+ Test)
- [ ] API Rest with Twisted for wait orders from Irianas Server, to do changes on the config files services. (+ Test)
- [x] Class for basic task on the system (Restart, Shutdown)
- [ ] Monitor System
- [ ] API Rest for basic task (+ Test)
- [x] Class for events system (Installation software, new updates, etc) (+ Test)
- [ ] Class for user creation, update and delete.
- [x] Class for admin services (Ex: Add VHOST on Apache, Add new user to FTP services) (+ Test)
