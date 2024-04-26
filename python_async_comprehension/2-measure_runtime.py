#!/usr/bin/env python3
"""module that measures the times of executing 4 processes"""

import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures the total runtimeof four process at a time

    Returns:
        float: The total runtime in seconds
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.perf_counter()
    total_time = end - start

    return total_time
