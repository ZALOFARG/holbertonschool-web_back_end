#!/usr/bin/env python3
"""module that takes a generator and returns a list"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine that returns a list of 10 random floats

    Returns:
        List: a list of 10 random float numbers
    """
    lst = [i async for i in async_generator()]
    return lst
