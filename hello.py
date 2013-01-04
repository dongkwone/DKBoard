from flask import Flask
import os


app = Flask(__name__)


@app.route("/")
def hello():
    return 'hello world yo'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0'
    app.run(host=host, port=port)
