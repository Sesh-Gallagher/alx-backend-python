#!/usr/bin/env python3
"""
Module that Annotate the below function’s parameters
and return values with the appropriate types
Duck type iterable object
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args: lst - sequence of the list

    Return: List of tuple of sequence of int
    """

    return [(a, len(a)) for a in lst]
