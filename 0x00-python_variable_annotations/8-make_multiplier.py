#!/usr/bin/env python3
"""
Module to write a type-annotated function make_multiplier
that takes a float multiplier as argument and returns
a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args: Multiplier: Factor

    Return: result of multiplier in float
    """

    def x(num: float):
        return num * multiplier
    return x
