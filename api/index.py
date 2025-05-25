import json
from urllib.parse import parse_qs

# Load student marks from the JSON file at deploy time
with open("q-vercel-python.json") as f:
    STUDENT_MARKS = json.load(f)

def handler(request):
    # Vercel uses 'event' with 'queryStringParameters'
    query = request.get("queryStringParameters", {})
    names = query.get("name", [])

    # If only one name is passed, wrap it in a list
    if isinstance(names, str):
        names = [names]

    marks = [STUDENT_MARKS.get(name, None) for name in names]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        },
        "body": json.dumps({"marks": marks})
    }

# Main entry point for Vercel
def handler(event, context):
    return handler(event)
