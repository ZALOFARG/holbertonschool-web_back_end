#!/usr/bin/env python3
"""Script that takes a str and a number int or float
and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """func takes 2 args and returns a tuple

    Args:
        k: string value
        v: int or float numb

    Returns:
        a tuple
    """
    return k, float(v**2)
