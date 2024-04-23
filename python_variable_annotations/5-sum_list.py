#!/usr/bin/env python3
"""Script that takes a list of floats
and returns its sum as float
"""


def sum_list(input_list: list[float]) -> float:
    """func takes a list and returns its sum

    Args:
        input_list: a list of floats

    Returns:
        a float that accumulates the list
    """
    acc: float = 0.0
    for elem in input_list:
        acc += elem

    return acc
