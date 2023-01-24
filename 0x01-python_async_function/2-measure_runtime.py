#!/usr/bin/env python3
import asyncio
from timeit import default_timer as timer
wait_n = __import__('1-concurrent_coroutines').wait_n
"""Measure the runtime"""


def measure_time(n: int, max_delay: float) -> int:
    """measures the total execution time for wait_n(n, max_delay)
    , and returns total_time / n"""
    start = timer()
    asyncio.run(wait_n(n, max_delay))
    end = timer()

    return (end - start) / n
