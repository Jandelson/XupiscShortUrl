from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, urljoin
from services.XupiscRegister import XupiscRegister
from services.XupiscShort import XupiscShort

class XupiscController(BaseHTTPRequestHandler):
    def do_GET(self):
        full_url = urljoin(XupiscShort._BASE_URL, self.path)

        xupiscRegister = XupiscRegister()
        url = xupiscRegister.get_original_url(full_url)
        if url:
            self.send_response(302)
            self.send_header('Location', url)
            self.end_headers()
        else:
            self.send_error(404, f"Short URL not found: {full_url}")