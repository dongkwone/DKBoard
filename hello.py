from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0'
    app.run(host=host, port=port)
