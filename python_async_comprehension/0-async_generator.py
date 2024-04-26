#!/usr/bin/env python3
"""module that produces a random generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator that yields 10 rand numb

    Yieldss:
        float: a rand number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
