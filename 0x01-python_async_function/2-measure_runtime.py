#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
from timeit import default_timer as timer

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time and returns total_time / n"""
    start = timer()
    asyncio.run(wait_n(n, max_delay))
    end = timer()

    return (end - start) / n
