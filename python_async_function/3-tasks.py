#!/usr/bin/env python3
"""creates and return a coroutine
"""
import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio.Task that waits for a rand delay

    Args:
        max_delay: max delay that it can be inhibited

    Returns:
        asyncio.Task
    """
    task1 = asyncio.create_task(wait_random(max_delay))
    return task1
