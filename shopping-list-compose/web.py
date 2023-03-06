from flask import Flask, jsonify, request
app = Flask(__name__)

items = []

class Item(object):
  def __init__(self, name, quantity):
    self.name = name
    self.quantity = quantity

@app.route("/", methods=["GET"])
def list_all():
  item_dicts = [
    { "name": item.name, "quantity": item.quantity } for item in items
  ]

  return jsonify(items=item_dicts)

@app.route("/add", methods=["POST"])
def add():
  name = request.json.get("name")
  quantity = request.json.get("quantity")

  if quantity < 1:
    return jsonify(error="Quantity must be at least 1"), 400

  items.append(Item(name, quantity))
  return jsonify({}), 200

@app.route("/clear", methods=["DELETE"])
def clear():
  items.clear()
  return jsonify({}), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
