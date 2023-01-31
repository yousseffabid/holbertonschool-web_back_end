#!/usr/bin/env python3
"""0-simple_helper_function module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """return start index and end index"""
    end_index = page * page_size
    return (end_index-page_size, end_index)
