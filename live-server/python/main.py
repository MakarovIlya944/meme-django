from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import traceback

class WatermelonServer(BaseHTTPRequestHandler):

    def do_GET(self):
        # Send response status code
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("hello !",encoding.base64))
        return

if __name__ == '__main__':
    server_address = ("localhost", 8080)
    httpd = ThreadingHTTPServer(server_address, WatermelonServer)
    print("INFO! Running server")
    httpd.serve_forever()
