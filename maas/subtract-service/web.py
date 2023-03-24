from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/subtract", methods=["GET"])
def subtract():
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
