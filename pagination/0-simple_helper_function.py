#!/usr/bin/python3
"""This module contains index_range()"""


def index_range(page, page_size):
    """Returns a tuple (start index, end index)"""
    return (page * page_size - page_size, page_size * page)