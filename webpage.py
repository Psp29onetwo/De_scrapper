from urllib import request

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        return render_template("data.html", code=request.form["code"])
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
