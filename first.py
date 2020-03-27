from flask import Flask, render_template, request, url_for, redirect
import priceHistoryUtils

# from werkzeug.utils import redirect
# to run the flask projrct in devcelopment mode set FLASK_ENV=development

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/your_url", methods=["GET", "POST"])
def your_url():
    if request.method == "POST":
        temp = request.form["code"]
        graph = priceHistoryUtils.plotter(temp)
        temp = graph
        return render_template("your_url.html", graph = temp)

    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
# TODO
#  Refactor and apply style to whole project and fullfill the requirement as shown in navbar with logo and all that.