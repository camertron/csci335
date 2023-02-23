from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:password@127.0.0.1:3306/shopping_list"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


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
