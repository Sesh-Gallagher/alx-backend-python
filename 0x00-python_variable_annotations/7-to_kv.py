#!/usr/bin/env python3
"""
Module to write a type-annotated function to_kv
that takes a string k and an int OR float v
as arguments and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Represents type-annotated function to_kv
    that takes a string k and an int OR floa
    """
    return (k, v * v)
