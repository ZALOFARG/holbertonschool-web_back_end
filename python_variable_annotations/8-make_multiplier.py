#!/usr/bin/env python3
"""Script that defines 'make_multiplier' function
which takes a float as argument
and returns a function that multiplies
a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """func takes a multiplier and use it in a callable funct

    Args:
        multiplier: numbt o be used as a multiplier

    Returns:
        a callable function
    """
    def mult_function(x: float) -> float:
        return x * multiplier

    return mult_function
