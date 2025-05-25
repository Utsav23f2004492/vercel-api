import json
import os

# Load JSON once
with open(os.path.join(os.path.dirname(__file__), '../q-vercel-python.json')) as f:
    data = json.load(f)

def handler(request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json"
    }

    query = request.get("query", {})
    names = query.get("name", [])
    if isinstance(names, str):
        names = [names]

    marks = [data.get(name, -1) for name in names]

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"marks": marks})
    }

