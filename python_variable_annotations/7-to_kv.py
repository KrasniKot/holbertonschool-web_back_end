#!/usr/bin/env python3
"""This module contains to_kv()"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, float(v**2))
