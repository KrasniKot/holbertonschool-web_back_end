#!/usr/bin/env python3
"""This module contains wait_n()"""

from asyncio import as_completed
from typing import List
waitom = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all the delays"""

    dlays = []
    tasks = []

    for time in range(n):
        tasks.append(waitom(max_delay))
    for task in as_completed(tasks):
        dlays.append(await(task))
    return dlays
