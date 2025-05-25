import json
import os

# Load data once
with open(os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')) as f:
    data = json.load(f)

def handler(request):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",  # Allow all origins
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    # Handle preflight OPTIONS request for CORS
    if request.method == "OPTIONS":
        return {
            "statusCode": 204,
            "headers": headers,
            "body": ""
        }

    # Parse query parameters safely
    query_params = request.args or {}

    # 'name' parameter can be single string or list
    names = query_params.getlist("name") if hasattr(query_params, "getlist") else query_params.get("name")
    
    if isinstance(names, str):
        # single name string
        names = [names]
    elif not names:
        names = []

    marks = [data.get(name, 0) for name in names]

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"marks": marks})
    }
