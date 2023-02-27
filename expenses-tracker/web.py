from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:password@127.0.0.1:3306/shared_expenses"
db = SQLAlchemy(app)

@app.route("/groups", methods=["POST"])
def create_group():
  return jsonify({})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
