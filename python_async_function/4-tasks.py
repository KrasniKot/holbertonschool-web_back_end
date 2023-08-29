#!/usr/bin/env python3
"""This module contains almost wait_n()"""

from asyncio import as_completed
from typing import List
waitom = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all the delays"""

    dlays = []
    tasks = []

    for time in range(n):
        tasks.append(waitom(max_delay))
    for task in as_completed(tasks):
        dlays.append(await(task))
    return dlays
