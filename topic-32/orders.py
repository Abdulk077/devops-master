from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request, time

failures = 0
circuit_open = False

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        global failures, circuit_open

        if circuit_open:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'CIRCUIT OPEN: returning cached response instantly')
            return

        try:
            urllib.request.urlopen('http://payments:8001', timeout=2)
        except:
            failures += 1
            if failures >= 3:
                circuit_open = True
            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                f'Payment failed. Failures: {failures} Circuit: {"OPEN" if circuit_open else "CLOSED"}'.encode()
            )
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Payment success')

    def log_message(self, *a): pass

HTTPServer(('', 8000), H).serve_forever()