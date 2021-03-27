"""
Multiple endpoints with CherryPy.

Based on
    http://stackoverflow.com/questions/14661217/running-more-than-one-class-in-cherrypy
"""
import cherrypy


class Root(object):
    def index(self):
        return "Hello, world!"
    index.exposed = True


class Admin(object):
    def index(self):
        """
        /admin
        """
        return 'Admin index'
    index.exposed = True

    def user(self, name=""):
        """
        /admin/user/{username}
        """
        return "You asked for user '%s'" % name
    user.exposed = True


class Search(object):
    def index(self):
        print 'start search'
        return self._calc()
    index.exposed = True
    
    def _calc(self):
        print 'calculating'
        return 'search results...'


cherrypy.root = Root()

# /admin or /admin/user/abc 
cherrypy.root.admin = Admin()

# /admin/search
cherrypy.root.admin.search = Search()

# /search
cherrypy.root.search = Search()


# This gives access to root and below.
# If you use Root() you don't get the subpaths.
cherrypy.tree.mount(cherrypy.root, '')

cherrypy.engine.start()
cherrypy.engine.block()
