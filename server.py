from http.server import HTTPServer, BaseHTTPRequestHandler
import time, re

HOST = "localhost"
PORT = 8000


class ServerHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        # Cache request
        path = self.path

        # Validate request path, and set type
        if path == "/resources/index.html":
            content_type = "text/html"
        elif path == "/resources/index.js":
            content_type = "text/javascript"
        elif path == "/resources/styles.css":
            content_type = "text/css"
        elif "/resources/img" in path:
            content_type = "image/jpeg"
        else:
            # Wild-card/default
            if not path == "/":
                print("UNRECONGIZED REQUEST:", path)

            path = "/resources/index.html"
            content_type = "text/resources"

        # Set header with content type
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()

        # Open the file, read bytes, serve
        with open(path[1:], 'rb') as file:
            self.wfile.write(file.read())  # Send

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))


server = HTTPServer((HOST, PORT), ServerHTTP)
print("Server now running...")

server.serve_forever()
server.server_close()
print("Server stopped")
