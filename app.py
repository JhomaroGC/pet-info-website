from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hola Jhoma!</p>"


if (__name__) == "__main__":
    app.run(port=3001, debug=True)
