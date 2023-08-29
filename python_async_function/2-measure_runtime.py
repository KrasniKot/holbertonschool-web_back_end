#!/usr/bin/env python3
"""This module contains measure_time()"""

from asyncio import run
from time import time
wain = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the execution time it took to execute wain()"""
    start = time()
    run(wain(n, max_delay))
    end = time()
    return ((end - start) / n)
