from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import socket
import time

def wait_for_db():
  s = socket.socket()
  tries = 0

  while True:
    try:
      s.connect(("db", 3306))
      break
    except Exception as e:
      tries += 1

      if tries > 5:
        raise e

      print("Waiting for database...")
      time.sleep(2)

  s.close()

wait_for_db()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://shopper:password@db:3306/shopping_list"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# create items table (if it doesn't exist)
with open("01_create_items.sql") as f:
  with app.app_context() as context:
    db.session.execute(text(f.read()))


class ItemRecord(db.Model):
  __tablename__ = "items"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  quantity = db.Column(db.Integer, nullable=False)


@app.route("/", methods=["GET"])
def list_all():
  item_dicts = [
    { "name": item.name, "quantity": item.quantity }
    for item in ItemRecord.query.all()
  ]

  return jsonify(items=item_dicts)

@app.route("/add", methods=["POST"])
def add():
  name = request.json.get("name")
  quantity = request.json.get("quantity")

  if quantity < 1:
    return jsonify(error="Quantity must be at least 1"), 400

  item = ItemRecord(name=name, quantity=quantity)
  db.session.add(item)
  db.session.commit()

  return jsonify({}), 200

@app.route("/clear", methods=["DELETE"])
def clear():
  ItemRecord.query.delete()
  db.session.commit()
  return jsonify({}), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
