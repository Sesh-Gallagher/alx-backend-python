#!/usr/bin/env python3
"""
Module that that spawns Tasks n times with a
specified delay between each call.
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args: n: number of times to spawn wait_random
         max_delay: maximum delay between each call
    Returns: list of delays
    """
    task_delay = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(task_delay)]
