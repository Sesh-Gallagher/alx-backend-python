#!/usr/bin/env python3
"""
Module to write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mixd_lst: List[Union[int, float]]) -> float:
    """
    Args: mixd_lst: float-int numrs


    Return: float base in int or floar numbrs
    """

    result: float = 0

    for a in mixd_lst:
        result += a

    return result
