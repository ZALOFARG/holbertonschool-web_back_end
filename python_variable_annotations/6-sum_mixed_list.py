#!/usr/bin/env python3
"""Script that takes a list of mix types
and returns its sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """func takes a list and returns its sum

    Args:
        mxd_lst: a list of floats and ints

    Returns:
        a float that accumulates the list
    """
    acc: float = 0.0
    for elem in mxd_lst:
        acc += elem

    return acc
