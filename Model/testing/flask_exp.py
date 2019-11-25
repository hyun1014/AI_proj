from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route("/admin")
def hello_admin():
    return "Hello admin!"


@app.route("/guest/<name>")
def hello_guest(name):
    return "Hello {}!".format(name)


@app.route("/nameis/<name>")
def hello(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", name=name))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("hello_guest", name=user))
    else:
        user = request.args.get("nm")
        return redirect(url_for("hello_guest", name=user))


if __name__ == "__main__":
    app.run(debug=True)
