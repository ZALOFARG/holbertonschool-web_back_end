#!/usr/bin/env python3

"""Server class pagination"""

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


    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """function that return a tuple containing a start index and a end index

        Args:
            page:
            page_size:

        Returns:
            int tuple
        """

        multi = page * page_size

        return (multi - page_size, multi)

    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """funct that determines the correct indexes to paginate the dataset

        Args:
            page: self explanatory
            page_size:self explanatory

        Returns:
            correct list of rows
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]




