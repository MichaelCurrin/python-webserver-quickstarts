#!/usr/bin/env python
"""
Hello world HTTP app using Cherrpy.
"""
import cherrypy


class HelloWorld(object):
    
    @cherrypy.expose
    def index(self):
        return "Hello World!"


if __name__ == '__main__':
    cherrypy.config.update(
        {'server.socket_port': 5000}
    )
    cherrypy.quickstart(HelloWorld())
