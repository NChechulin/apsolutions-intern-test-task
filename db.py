from os.path import exists as file_exists
from sqlite3 import Connection, Cursor, InterfaceError, connect
from typing import List

from post import Post

GET_POST_IDS_BY_TEXT_QUERY = """
SELECT id
FROM posts_index
WHERE text MATCH ?
LIMIT 20"""
GET_POST_BY_ID_QUERY = """
SELECT *
FROM posts
WHERE id = ?
"""
DELETE_POST_BY_ID_QUERY = """
DELETE
FROM posts
WHERE id = ?
"""


class Database:
    connection: Connection = None
    cursor: Cursor = None

    def __init__(self, db_path: str):
        if not file_exists(db_path):
            raise Exception("Specified database file does not exist")

        self.connection = connect(db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def try_delete_post_by_id(self, post_id: int):
        """
        Tries to delete post by it's id.
        Raises Exception if id is incorrect.
        """
        # check if post with this id exists
        # if not, exception will be raised
        # this is needed because sqlite doesn't throw exceptions
        # when you try to delete row which doesn't exist
        self.__get_post_by_id(post_id)
        # actual deletion of the row
        self.cursor.execute(DELETE_POST_BY_ID_QUERY, (post_id,)).fetchone()
        self.connection.commit()

    def __get_post_ids_by_text(self, search_text: str) -> List[int]:
        """
        Returns list of ids of posts which match search_text
        """
        ids = self.cursor.execute(GET_POST_IDS_BY_TEXT_QUERY, (search_text,))
        # unpack list of tuples to list: [(1,), (2,), (3,)] -> [1, 2, 3]
        return [tpl[0] for tpl in ids]

    def __get_post_by_id(self, id: int) -> Post:
        """
        Returns post by it's id
        """
        raw_post = self.cursor.execute(GET_POST_BY_ID_QUERY, (id,)).fetchone()
        if raw_post:
            return Post(*raw_post)
        raise Exception("There is no post with such id")

    def get_posts_by_text(self, search_text: str, to_fetch=20) -> List[Post]:
        """
        Returns list of 20 (or less) posts found which contain `search_text`
        """
        post_ids = self.__get_post_ids_by_text(search_text)
        return [self.__get_post_by_id(id) for id in post_ids]

    def __del__(self):
        self.cursor.close()
        self.connection.close()