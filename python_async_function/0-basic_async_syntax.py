#!/usr/bin/env python3
"""async coroutine that returns a number
waiting the same time in sec
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async func that returns a number and waits
    the exact time

    Args:
        max_delay: max delay that it can be inhibited

    Returns:
        the random number generated
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
