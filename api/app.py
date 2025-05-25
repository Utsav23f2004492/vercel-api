from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Parse query parameters
            query = urlparse(self.path).query
            params = parse_qs(query)
            
            # Get names from query parameters
            names = params.get('name', [])
            
            # Load marks data
            with open(os.path.join(os.path.dirname(__file__), 'data.json')) as f:
                data = json.load(f)
            
            # Create name to marks mapping
            marks_dict = {item['name']: item['marks'] for item in data}
            
            # Get marks for requested names
            results = []
            for name in names:
                results.append(str(marks_dict.get(name, "Not found")))
            
            # Set CORS headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Prepare response
            response = {
                "marks": " ".join(results)
            }
            
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())