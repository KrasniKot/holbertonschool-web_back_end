#!/usr/bin/env python3
"""This module contains async_comprehension"""

from typing import List
asgen = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 random numbers"""
    ns = [n async for n in asgen()]
    return ns
