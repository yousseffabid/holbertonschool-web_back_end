#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """A task duration is approximately 2,5 seconds """
    tasks = []
    start = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
