#!/usr/bin/env python3
"""
Module that represents the method that spawns wait_random
n times witha specific delay between each call
"""

from typing import List
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args: max_delay: max wait
          n: spawn func

    Return: float time random
    """

    task = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    end = [await task for task in asyncio.as_completed(task)]
    return end
