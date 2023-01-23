#!/usr/bin/env python3
"""duck type an iterable object"""
from typing import List, Tuple, Iterable, Sequence 


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Element length """
    return [(i, len(i)) for i in lst]