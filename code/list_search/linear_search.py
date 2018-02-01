#!/usr/bin/env python
# encoding: utf-8

from hypothesis import given, settings
import hypothesis.strategies as st


def linear_search(search_list, item):
    """Search search_list from left to right for item.

    Parameters
    ----------
    search_list : list
        list to be searched
    item
        item we are looking for

    Returns
    -------
    int or False

    Examples
    --------
    >>> linear_search([0,1,7,9], 7)
    2

    >>> linear_search([0,1,7,9], 8)
    False
    """
    for i in range(len(search_list)):
        if item == search_list[i]:
            return i
    return False


@given(search_list=st.lists(st.integers()),
       item=st.integers())
@settings(max_examples=10000)
def test_binary_search(search_list, item):
    if item in search_list:
        pos = linear_search(search_list, item)
        assert search_list[pos] == item
    else:
        assert linear_search(search_list, item) is False
