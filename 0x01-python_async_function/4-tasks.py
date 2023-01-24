#!/usr/bin/env python3
import asyncio
"""."""
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """returns list of delayed async tasks"""
    tasks = []
    result_list = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    result_list = [await task for task in asyncio.as_completed(tasks)]
    return result_list
