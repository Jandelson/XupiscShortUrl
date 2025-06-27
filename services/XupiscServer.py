from http.server import BaseHTTPRequestHandler, HTTPServer
from views.XupiscController import XupiscController

def run(server_class=HTTPServer, port=8086):
        server_address = ('', port)
        httpd = server_class(server_address, XupiscController)
        print(f'Starting Xupisc URL Shortener on port {port}...')
        httpd.serve_forever()

if __name__ == "__main__":
    run()