#!/usr/bin/env python3
"""This module contains make_multiplier()"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns prod()"""
    def prod(x: float) -> float:
        """Returns the product"""
        return float(multiplier * x)
    return prod
