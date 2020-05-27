#!/usr/bin/env python
"""
Hello World web app - with no framework.

Based on:
    https://docs.python.org/3.9/library/http.server.html?highlight=base%20http
    https://dfpp.readthedocs.io/en/latest/chapter_01.html

Dedent is used to remove all common whitespace in the output.

To serve the directory a files, set SimpleHTTPRequestHandler as the request
handler rather than HelloRequestHandler.
"""
import textwrap
from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Handle HTTP GET request on root with HTML greeting or a not found error.
        """
        if self.path != '/':
            self.send_error(404, "Page not found")
            
            return

        self.send_response(200)
        
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        response_text = textwrap.dedent("""\
            <html>
            
            <head>
                <title>Greetings to the World</title>
            </head>
            
            <body>
                <h1>Greetings to the World</h1>
                <p>Hello, world!</p>
                
            </body>
            
            </html>
        """)
        
        self.wfile.write(response_text.encode('utf-8'))


def run(port=5000):
    """
    Start HTTP server.
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, HelloRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
