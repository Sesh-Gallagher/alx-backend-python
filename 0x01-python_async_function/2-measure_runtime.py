#!/usr/bin/env python3
"""
Module represents a method that measure the total execution
time of a function
"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
       n: the number of coroutines to launch
    max_delay: max amount of time to wait for each coroutine

    returns: time elapsed in seconds
    """

    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    Total_time = perf_counter() - start
    return Total_time / n
