import unittest
from json import loads

from app import app as api


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = api.test_client()

    def test_succesful_deletion(self):
        """
        Checks that record can be succesfully deleted
        """
        response = self.app.delete("/delete_record?id=179").data.decode()
        assert response == "Success"

    def test_no_deletion_of_one_post_twice(self):
        """
        Cheks that same record can not be deleted twice
        """
        response = self.app.delete("/delete_record?id=179").data.decode()
        assert response == "There is no post with such id"

    def test_deletion_of_invalid_id(self):
        """
        Check that non-existing record cannot be deleted
        """
        response = self.app.delete("/delete_record?id=123456").data.decode()
        assert response == "There is no post with such id"

    def test_get_ids_match(self):
        """
        Checks that get_posts returns correct results
        """
        response = self.app.get("/get_posts?query=собака").data.decode()
        # get ids of posts from response
        post_ids = [post["id"] for post in loads(response)]
        assert post_ids == [147, 723, 1048]

    def test_get_ids_match_after_deletion(self):
        """
        Checks that deleted record don't show up in posts_results
        """
        self.app.delete("/delete_record?id=147")
        response = self.app.get("/get_posts?query=собака").data.decode()
        # get ids of posts from response
        post_ids = [post["id"] for post in loads(response)]
        assert post_ids == [723, 1048]


if __name__ == "__main__":
    unittest.main()
