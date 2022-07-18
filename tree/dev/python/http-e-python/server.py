# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("HTTP method", "GET")
        self.send_header("Example", "xD")

        print("\n")
        print(type(self.headers))
        print(self.headers)
        # print(self.headers['X-MyHeader'])
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>just-http</title></head>", "utf-8"))
        self.wfile.write(
            bytes("<p><b>Request path</b>: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(
            bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(
            bytes("<p><b>Headers received</b>: %s</p>" % self.headers, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(201)
        self.send_header("Content-type", "text/html")
        self.send_header("HTTP method", "POST")
        print("\n")
        print(type(self.headers))
        print(self.headers)
        
        # Body
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        print(body.decode("utf-8"))
        print(type(body.decode("utf-8")))
        json_body= json.loads(body.decode("utf-8"))
        print(type(json_body))
        print(json_body['Id'])

        # print(self.headers['X-MyHeader'])
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>just-http</title></head>", "utf-8"))
        self.wfile.write(
            bytes("<p><b>Request path</b>: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(
            bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(
            bytes("<p><b>Headers received</b>: %s</p>" % self.headers, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
