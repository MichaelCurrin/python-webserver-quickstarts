#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-
"""
Multiple endpoints with CherryPy.

Alternate script that works on PythonAnywhere.com site.
"""
import random
import socket
import string
import sys

import cherrypy

sys.stdout = sys.stderr
cherrypy.log('START')


class Root(object):
    def index(self):
        return "Hello, world!"
    index.exposed = True


class Admin(object):
    # no /admin only /admin/user/abc
    def user(self, name=""):
        return "You asked for user '%s'" % name
    user.exposed = True


class Search(object):
    # /admin/search
    def index(self):
        return 'search results'
    index.exposed = True

cherrypy.root = Root()
cherrypy.root.admin = Admin()
cherrypy.root.admin.search = Search()


cherrypy.log('Mounting app')

# `app` object as set in wsgi file
app = cherrypy.Application(cherrypy.root, 
    script_name='', 
    config={
        'global':
            {
            'environment': 'embedded',
            #'server.socket_port': 9090,
            },
        }
    )

print socket.getfqdn()

if socket.getfqdn() != 'localhost': 
    # Use this to start app if we are not on PythonAnywhere
    cherrypy.engine.start()
    cherrypy.engine.block()
