from ast import literal_eval
from datetime import datetime
from typing import List

DATETIME_PATTERN = r"%Y-%m-%d %H:%M:%S"


class Post:
    """
    Container which represents one post.
    """

    id: int = None
    text: str = None
    # These parameters are being converted to datetime and list respectively
    # in order to give more flexibility to the service in future.
    # In current version they will be converted back to string later.
    created_date: datetime = None
    rubrics: List[str] = None

    def __init__(self, id: int, text: str, raw_date: str, raw_rubrics: str):
        self.id = id
        self.text = text
        self.created_date = datetime.strptime(raw_date, DATETIME_PATTERN)
        # safe conversion of string representation of list to actual list
        self.rubrics = literal_eval(raw_rubrics)
