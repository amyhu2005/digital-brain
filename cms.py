import http.server
import json
import os

class CMSHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            filename = data.get('filename')
            content = data.get('content')
            
            if filename and content:
                # Sanitize filename to prevent directory traversal
                safe_filename = os.path.basename(filename)
                with open(safe_filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode())
            else:
                self.send_error(400, "Missing filename or content")

if __name__ == "__main__":
    print("Admin Server started at http://localhost:8000")
    print("Press Alt + A on your website to start editing!")
    http.server.HTTPServer(('0.0.0.0', 8000), CMSHandler).serve_forever()
