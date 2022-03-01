import logging

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":

    host_ip = "0.0.0.0"  # noqa: S104
    host_port = "5000"

    app.run(host=host_ip, port=host_port)
