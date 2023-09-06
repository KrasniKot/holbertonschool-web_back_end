#!/usr/bin/env python3
"""This module contains index_range()"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple (start index, end index)"""
    return (page * page_size - page_size, page_size * page)
