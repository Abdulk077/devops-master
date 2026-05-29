from http.server import HTTPServer, BaseHTTPRequestHandler
import time

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(5)
        self.send_response(500)
        self.end_headers()
        self.wfile.write(b'payment failed')
    def log_message(self, *a): pass

HTTPServer(('', 8001), H).serve_forever()