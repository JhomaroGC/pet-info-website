from flask import Flask, render_template, jsonify
from data import read_data



app = Flask(__name__)

data = read_data()


@app.route("/")
def hello_world():
    return render_template('index.html', data=data)

@app.route("/api/pets")
def pet_list():
    return jsonify(data)


if (__name__) == "__main__":
    app.run(port=3001, debug=True)
