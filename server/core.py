# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import http.server
import socketserver
import os
import socket

class SimpleServer:
    def __init__(self, port=8000, directory=".", bind="0.0.0.0"):
        self.port = port
        self.directory = os.path.abspath(directory)
        self.bind = bind

    def start(self):
        if not os.path.isdir(self.directory):
            print(f"Error: Directory '{self.directory}' does not exist.")
            return

        # Change to the directory we want to serve
        os.chdir(self.directory)

        Handler = http.server.SimpleHTTPRequestHandler

        # Create the server
        try:
            with socketserver.TCPServer((self.bind, self.port), Handler) as httpd:
                print(f"Serving HTTP on {self.bind} port {self.port} (http://{self.bind}:{self.port}/) ...")
                print(f"Serving directory: {self.directory}")
                print("Press Ctrl+C to stop.")
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\nServer stopped.")
                    httpd.server_close()
        except OSError as e:
            if e.errno == 98 or e.errno == 48: # Address already in use
                print(f"Error: Port {self.port} is already in use.")
            else:
                print(f"Error starting server: {e}")

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
