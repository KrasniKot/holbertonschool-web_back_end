#!/usr/bin/python3
"""This module contains async_generator()"""

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[int, None, None]:
    """Yields 10 random numbers"""
    for time in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
