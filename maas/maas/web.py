from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/evaluate", methods=["GET"])
def evaluate():
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
