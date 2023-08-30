#!/usr/bin/env python3
"""This module contains measure_runtime()"""

import asyncio
from time import time
asco = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns 10 random numbers"""
    begin = time()
    tasks = [asco() for i in range(4)]
    await asyncio.gather(*tasks)
    end = time()
    return end - begin
