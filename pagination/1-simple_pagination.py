#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """def that returns a list containing the range
        specified in the tuple passed"""
        assert type(page) is int and type(page_size) is int
        assert page > 0
        assert page_size > 0
        self.dataset()

        tup = index_range(page, page_size)

        if tup[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[tup[0]:tup[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''funct that returns a tuple containing
    start and ending indexes
    '''

    index = page * page_size - page_size
    index_1 = index + page_size
    return (index, index_1)
