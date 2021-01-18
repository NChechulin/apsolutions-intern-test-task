from os.path import exists as file_exists
from sqlite3 import Connection, Cursor, connect
from typing import List

from post import Post


class Database:
    connection: Connection = None
    cursor: Cursor = None

    def __init__(self, db_path: str):
        if not file_exists(db_path):
            raise Exception("Specified database file does not exist")

        self.connection = connect(db_path)
        self.cursor = self.connection.cursor()

    def try_delete_post_by_id(self, post_id: int):
        """
        Tries to delete post by it's id.
        Raises Exception if id is incorrect.
        """
        pass

    def get_posts_by_text(self, search_text: str, to_fetch=20) -> List[Post]:
        """
        Returns list of 20 (or less) posts found which contain `search_text`
        """
        pass
