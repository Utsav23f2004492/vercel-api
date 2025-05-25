from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/api', methods=['GET'])
def get_marks():
    name = request.args.get('name')
    if name == 'X':
        return jsonify({"marks": [10, 20]})
    elif name == 'Y':
        return jsonify({"marks": [20, 10]})
    return jsonify({"error": "Name not found"}), 404

if __name__ == "__main__":
    app.run()