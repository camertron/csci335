from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlalchemy
import os
import socket
import time

mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_host = os.getenv("MYSQL_HOST")
mysql_port = int(os.getenv("MYSQL_PORT"))
mysql_database = os.getenv("MYSQL_DATABASE")
mysql_url = (
  f"mysql+mysqldb://{mysql_user}:{mysql_password}"
  f"@{mysql_host}:{mysql_port}/{mysql_database}")

def wait_for_db():
  s = socket.socket()
  s.settimeout(1)
  tries = 0

  while True:
    try:
      s.connect((mysql_host, mysql_port))
      break
    except Exception as e:
      tries += 1

      if tries > 6:
        raise e

      print("Waiting for database...", flush=True)
      time.sleep(3)

  s.close()

wait_for_db()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = mysql_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# create items table (if it doesn't exist)
with app.app_context() as context:
  with open("01_create_database.sql") as f:
    query = f.read().replace("{{MYSQL_DATABASE}}", mysql_database)
    db.session.execute(text(query))

  with open("02_create_items.sql") as f:
    query = f.read().replace("{{MYSQL_DATABASE}}", mysql_database)
    db.session.execute(text(query))


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

  return render_template("list.html", items=item_dicts)

@app.route("/new", methods=["GET"])
def new():
  return render_template("new.html", name=None, quantity=None)

@app.route("/add", methods=["POST"])
def add():
  name = request.form.get("name")
  quantity = request.form.get("quantity")

  if quantity.isnumeric():
    quantity = int(quantity)
  else:
    quantity = 0

  if quantity < 1:
    return render_template("new.html", name=name, quantity=quantity, error="Quantity must be at least 1"), 400

  if not name:
    return render_template("new.html", name=name, quantity=quantity, error="Name cannot be blank"), 400

  item = ItemRecord(name=name, quantity=quantity)
  db.session.add(item)
  db.session.commit()

  return redirect("/")

@app.route("/clear", methods=["POST"])
def clear():
  ItemRecord.query.delete()
  db.session.commit()
  return redirect("/")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
