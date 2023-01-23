#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument
    returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return multiplier_function
