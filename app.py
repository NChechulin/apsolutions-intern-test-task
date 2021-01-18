from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/delete_record", methods=["GET"])
def delete_record_handler():
    return "not ready yet..."


@app.route("/get_records", methods=["GET"])
def get_records_handler():
    return "not ready yet..."


if __name__ == "__main__":
    app.run()
