from http.server import HTTPServer, BaseHTTPRequestHandler
import redis, time, json

r = redis.Redis(host='redis', port=6379)

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        cached = r.get('data')
        if cached:
            source = 'CACHE'
            result = cached.decode()
        else:
            time.sleep(2)  # simulates slow DB query
            result = 'Hello from the database!'
            r.setex('data', 10, result)  # cache for 10 seconds
            source = 'DATABASE'

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"<h2>Source: {source}</h2><p>{result}</p>".encode())

    def log_message(self, *a): pass

HTTPServer(('', 8000), H).serve_forever()