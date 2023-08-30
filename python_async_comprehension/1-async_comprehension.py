#!/usr/bin/env python3
"""This module contains async_comprehension"""

asgen = __import__("0-async_generator").async_generator
from asyncio import run
from typing import Generator

async def async_comprehension() -> Generator[float, None, None]:
    """Returns 10 random numbers"""
    ns = [n async for n in asgen()]    
    return ns   
