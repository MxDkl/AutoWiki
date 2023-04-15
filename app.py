from flask import Flask, redirect, render_template_string
import os

import gen


app = Flask(__name__)
app_dir = os.path.abspath(os.path.dirname(__file__))


@app.route("/")
def index():
    return redirect("/index.html")

@app.route("/<path:path>", methods=["GET"])
def catch_all(path):
    # if the path exists, return the path
    # if the path doesn't exist, return the generated path
    site_path = os.path.join(app_dir, "site", path.split('.')[0] + ".html")
    if os.path.exists(site_path):
        with open(site_path, "r") as file:
            content = file.read()
    else:
        content = gen.genDoc(path)
        os.makedirs(os.path.dirname(site_path), exist_ok=True)
        with open(site_path, "w") as file:
            file.write(content)

    return render_template_string(content)