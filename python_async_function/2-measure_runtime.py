#!/usr/bin/env python3
"""creates a func that determines the avg time
of a successive function calls
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the avg time it takes for wait_n to complete

    Args:
        n: number of times to spawn funct
        max_delay: max delay that it can be inhibited

    Returns:
        average time
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
