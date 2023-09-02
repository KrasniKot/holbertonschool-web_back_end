#!/usr/bin/env python3
"""This module contains safe_first_element()"""

from typing import List, Any


# The types of the elements of the input are not know
def safe_first_element(lst: List[Any]) -> Any:
    if lst:
        return lst[0]
    else:
        return None
