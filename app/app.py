import asyncio
from json import dumps
from os import getenv
from flask import Flask, request
from .db import Database

loop = asyncio.get_event_loop()
app = Flask(__name__)
db = Database(getenv("APPLICATION_DB_PATH"))


@app.route("/delete_record", methods=["DELETE"])
def delete_record_handler():
    try:
        id = int(request.args["id"])
        loop.run_until_complete(db.try_delete_post_by_id(id))
        return "Success"
    except Exception as exc:
        return str(exc)


@app.route("/get_posts", methods=["GET"])
def get_posts_handler():
    try:
        query = request.args["query"]
        posts = loop.run_until_complete(db.get_posts_by_text(query))
        return dumps([post.as_dict() for post in posts])
    except Exception as exc:
        return str(exc)


if __name__ == "__main__":
    app.run()
