#!/usr/bin/env python3
"""
Module write a type-annotated function sum_list
which takes a list input_list of floats
as argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args: input_list: float numbers

    Return: Sum of the float
    """

    result: float = 0

    for a in input_list:
        result += a

    return result
