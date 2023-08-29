#!/usr/bin/env python3:
"""This module contains element_lenght()"""

from typing import


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function to annotate"""
    return [(i, len(i)) for i in lst]
