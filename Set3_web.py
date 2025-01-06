from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the handler class to serve the HTML page
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML content for the root URL
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # The HTML content to serve
            html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Welcome to My Web Server</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p>Welcome to my web server powered by Python!</p>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode('utf-8'))
        else:
            # Handle other paths by serving a 404 error
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 - Page Not Found")

# Define the host and port
host = 'localhost'
port = 8080

# Start the web server
with HTTPServer((host, port), MyHandler) as server:
    print(f"Serving on http://{host}:{port}")
    server.serve_forever()
