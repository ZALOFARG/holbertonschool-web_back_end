#!/usr/bin/env python3
"""creates a async coroutine that uses
the 0-basic_async_syntax module
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async func that spawns wait_random n times
    with the specified max_delay

    Args:
        n: number of times
        max_delay: max delay that it can be inhibited

    Returns:
        List of floats generated
    """
    delays = []
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
