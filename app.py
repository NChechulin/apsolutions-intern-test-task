from json import dumps
from flask import Flask, request
from db import Database

app = Flask(__name__)
db = Database("documents.sqlite")


@app.route("/delete_record", methods=["GET"])
def delete_record_handler():
    try:
        id = int(request.args["id"])
        db.try_delete_post_by_id(id)
        return "Success"
    except Exception as exc:
        return str(exc)


@app.route("/get_posts", methods=["GET"])
def get_posts_handler():
    return "not ready yet..."


if __name__ == "__main__":
    app.run()
