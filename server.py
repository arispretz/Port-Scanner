import http.server
import socketserver
from port_scanner import get_open_ports

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/results':
            with open('results.txt', 'r') as file:
                results = file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(results.encode())
            return
        return super().do_GET()

PORT = 3000

# Run port scans and save results to results.txt
with open('results.txt', 'w') as file:
    # Called with URL
    ports = get_open_ports("www.freecodecamp.org", [75, 85])
    file.write(f"Open ports: {ports}\n")

    # Called with IP address
    ports = get_open_ports("104.26.10.78", [8079, 8090])
    file.write(f"Open ports: {ports}\n")

    # Verbose called with IP address and no host name returned -- single open port
    ports = get_open_ports("104.26.10.78", [440, 450], True)
    file.write(f"{ports}\n\n")

    # Verbose called with IP address and valid host name returned -- single open port
    ports = get_open_ports("137.74.187.104", [440, 450], True)
    file.write(f"{ports}\n\n")

    # Verbose called with host name -- multiple ports returned
    ports = get_open_ports("scanme.nmap.org", [20, 80], True)
    file.write(f"{ports}\n\n")

# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
