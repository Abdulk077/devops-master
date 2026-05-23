from http.server import HTTPServer, BaseHTTPRequestHandler
import socket, os

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(
            f"<h2>Request handled by: {socket.gethostname()}</h2>".encode()
        )
    def log_message(self, *a): pass

HTTPServer(('', 8000), H).serve_forever()