import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler
from typing import List

# Load the students marks data once
with open("q-vercel-python.json") as f:
    STUDENT_MARKS = json.load(f)


def handler(request):
    # request is a Vercel request object with .method and .url

    # Parse query string from request.url
    # URL format: /api?name=X&name=Y&name=Z ...
    query = request.url.split("?", 1)[-1] if "?" in request.url else ""
    params = parse_qs(query)

    # Extract all 'name' parameters (list of names)
    names = params.get("name", [])

    # Prepare marks list in same order
    marks = [STUDENT_MARKS.get(name, None) for name in names]

    # Prepare response JSON
    response = {"marks": marks}

    # Build HTTP response with CORS headers
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
    }

    return 200, headers, json.dumps(response)


# Vercel expects this exact entry point for Python API:
def main(request):
    status, headers, body = handler(request)
    return status, headers, body
