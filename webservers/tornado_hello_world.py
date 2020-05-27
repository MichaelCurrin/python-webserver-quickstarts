"""
Hello world HTTP app using Tornado.
"""
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    
    def get(self):
        """
        Handle GET request with greeting.
        """
        self.write("Hello, world!")


def make_app():
    routes = [
        (r"/", MainHandler) 
    ]
    
    return tornado.web.Application(routes)


def run(port=5000):
    """
    Start HTTP server.
    """
    app = make_app()
    app.listen(port)
    
    tornado.ioloop.IOLoop.current().start()



if __name__ == "__main__":
    run()
    
