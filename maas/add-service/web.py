from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["GET"])
def add():
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
