#!/usr/bin/env python3
# encoding: utf-8

from hypothesis import given, settings
import hypothesis.strategies as st


def binary_search(search_list, item):
    """Use binary search to find position of item in search_list.

    This algorithm is more efficient than linear search,
    but only works for sorted lists!

    Parameters
    ----------
    search_list : list
        list to be searched
    item : any
        item we are looking for

    Returns
    -------
    int or False

    Examples
    --------
    >>> binary_search([0,1,7,9], 7)
    2

    >>> binary_search([0,1,7,9], 8)
    False
    """
    start = 0
    end = len(search_list) - 1

    while start <= end:
        # pick middle element of list;
        # we use int() for rounding down
        middle = int(start + (end - start)/2)

        # Case 1: our item is to the left of the item at the midpoint,
        #         limit next search to left half
        if item < search_list[middle]:
            end = middle - 1
        # Case 2: our item is to the right of the item at the midpoint,
        #         limit next search to right half
        elif item > search_list[middle]:
            start = middle + 1
        # Case 3: we found our item, return its index
        elif item == search_list[middle]:
            return middle
    # Case 4: item not in list, while-loop aborted
    return False


@given(search_list=st.lists(st.integers()),
       item=st.integers())
@settings(max_examples=10000)
def test_binary_search(search_list, item):
    # we only care about sorted lists
    search_list = sorted(search_list)
    # now the actual tests
    if item in search_list:
        pos = binary_search(search_list, item)
        assert search_list[pos] == item
    else:
        assert binary_search(search_list, item) is False
