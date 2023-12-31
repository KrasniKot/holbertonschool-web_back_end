#!/usr/bin/env python3
"""This module ???"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple (start index, end index)"""
    return (page * page_size - page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the correspondent rows in list format"""
        assert type(page) == int and type(page_size) == int
        assert 0 < page and 0 < page_size

        lines = []

        with open("Popular_Baby_Names.csv", "r") as f:
            r = index_range(page, page_size)

            for idx, row in enumerate(f):
                if idx in range(r[0] + 1, r[1] + 1):
                    lines.append(row.strip().split(","))

        return lines

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing:
        the prev, next, and current page
        """
        rdict = {}
        rdict["page_size"] = len(get_page(page, page_size))
        return rdict
