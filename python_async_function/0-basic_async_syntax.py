#!/usr/bin/env python3
"""This module contains wait_random()"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Returns its argument after a random sleep time"""
    sleep_time = uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time

asyncio.run(wait_random())
