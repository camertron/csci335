from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:password@127.0.0.1:3306/chat_app"
db = SQLAlchemy(app)

@app.route("/users", methods=["POST"])
def create_user():
  return jsonify({})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
