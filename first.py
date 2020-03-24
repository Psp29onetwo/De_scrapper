from flask import Flask, render_template, request, url_for, redirect

# from werkzeug.utils import redirect
# to run the flask projrct in devcelopment mode set FLASK_ENV=development


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/your_url", methods=["GET", "POST"])
def your_url():
    if request.method == "POST":
        return render_template("your_url.html", code=request.form["code"])
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
