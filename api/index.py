import json
import os

with open(os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')) as f:
    data = json.load(f)

def handler(request):
    query = request.args
    names = query.getlist("name")
    marks = [data.get(name, 0) for name in names]
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps({ "marks": marks })
    }
