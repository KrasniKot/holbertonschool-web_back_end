#!/usr/bin/env python3
"""This mmodule contains task_wait_random()"""

import asyncio
waitom = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an ascyncio Task"""
    return asyncio.create_task(waitom(max_delay))
