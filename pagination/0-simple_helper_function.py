#!/usr/bin/env/python 3

"""Determines the range of pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that return a tuple containing a start index and a end index

    Args:
        page:
        page_size:

    Returns:
        int tuple
    """

    multi = page * page_size

    return (multi - page_size, multi)
