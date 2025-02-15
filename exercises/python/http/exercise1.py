"""
Simple HTTP server.
https://docs.python.org/3/library/http.server.html
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

class myHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    """
    HTTPRequestHandler class
    Parsing of the request is done by the base class BaseHTTPRequestHandler.
    """

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello world!"
        # Write message content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is Post request. ')
        response.write(b'Recieved')
        response.write(body)
        self.wfile.write(response.getvalue())


def main():
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, myHTTPServer_RequestHandler)
    print("running server...")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
