#!/usr/bin/env python3
"""
Module to import async_generator from the previous task
and then write a coroutine called async_comprehension
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine will collect 10 random numbers
    using an async comprehensing over async_generator
    """
    for a in range(10):
        await asyncio.sleep(1)
        yield random.unform(0, 10)
