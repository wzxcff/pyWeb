from http.server import HTTPServer, BaseHTTPRequestHandler
import time, re

HOST = "localhost"
PORT = 8000


class ServerHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/html/index.html":
            self.send_response(200, "main page")
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("html/index.html", "r") as file:
                content = file.read()

            self.wfile.write(bytes(content, "utf-8"))
        elif self.path == "/html/script.js":
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()
        elif self.path == "/html/style.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
        elif self.path == "/html/img/about.jpg":
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
        elif self.path == "/html/style.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes("<html><body><a href='main'>To main page!</a></body></html>", "utf-8"))


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
