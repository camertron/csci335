from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/groups", methods=["POST"])
def create_group():
  return jsonify({})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
