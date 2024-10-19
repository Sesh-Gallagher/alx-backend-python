#!/usr/bin/env python3
"""
Module to import async_generator from the previous task
and then write a coroutine called async_comprehension
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random numbers
    using an async comprehensing over async_generator
    """
    return ([a async for a in async_generator()])
