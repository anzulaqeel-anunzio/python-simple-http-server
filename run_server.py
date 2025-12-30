# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from server.core import SimpleServer

def main():
    parser = argparse.ArgumentParser(description="Simple HTTP Server CLI")
    parser.add_argument("--port", "-p", type=int, default=8000, help="Port to serve on (default: 8000)")
    parser.add_argument("--directory", "-d", default=".", help="Directory to serve (default: current directory)")
    parser.add_argument("--bind", "-b", default="0.0.0.0", help="Bind address (default: 0.0.0.0)")

    args = parser.parse_args()

    server = SimpleServer(port=args.port, directory=args.directory, bind=args.bind)
    server.start()

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
