#!/usr/bin/env python3
"""
Module to import async_comprehension from the previous file
write a measure_runtime coroutine
that will execute async_comprehension
"""

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should measure the total runtime and return it.

    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    stop = time.perf_counter()

    return (stop - start_time)
