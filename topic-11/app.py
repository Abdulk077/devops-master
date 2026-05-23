from http.server import HTTPServer, BaseHTTPRequestHandler
import socket, time

START_TIME = time.time()

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            uptime = time.time() - START_TIME
            if uptime < 10:
                self.send_response(503)
                self.end_headers()
                self.wfile.write(b'not ready yet')
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'healthy')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                f"<h2>Hello from {socket.gethostname()}</h2>".encode()
            )
    def log_message(self, *a): pass

HTTPServer(('', 8000), H).serve_forever()