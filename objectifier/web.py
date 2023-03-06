import base64
import os
import requests
import json

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path="", static_folder="static/")
app.config['UPLOAD_FOLDER'] = "static/uploads"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        img_data = base64.b64encode(request.files["file"].read()).decode("ascii")
        # 1. Make request to object detector with requests.post(...)
        # 2. Parse json response
        # 3. Get base64-encoded image data from response
        # 4. Decode image data
        # 5. Write image to a file
        filename = "nothing_yet"
        return render_template("home.html", image=filename)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
