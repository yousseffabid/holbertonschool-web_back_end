#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of floats and int as argument
    returns their sum as a float.
    """
    return sum(mxd_lst)
