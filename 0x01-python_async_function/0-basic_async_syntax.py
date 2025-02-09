#!/usr/bin/env python3
"""
Module represents asynchronous coroutine
that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:  max_delay: The maximum delay to return

    Returns:  random float between 0 and max_delay
    """

    dela = random.uniform(0, max_delay)
    await asyncio.sleep(dela)

    return dela
