from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home-redirect")   # redirection to home page
def home_redirect():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port = 5000, debug = True)
