#!/usr/bin/env python3
"""
Module that represents a function task_wait_random which
takes integer argument max_delay and return a asyncio.task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args: max_delay:  maximum number of seconds that the task will wait

    Returns: asyncio.Task object
    """

    stop = asyncio.create_task(wait_random(max_delay))
    return stop
