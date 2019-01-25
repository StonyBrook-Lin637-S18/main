#!/usr/bin/env python3
# encoding: utf-8

from hypothesis import given, settings
import hypothesis.strategies as st


def binary_search(search_list, item, start=0, end=None):
    """Use binary search to find position of item in search_list.

    This algorithm is more efficient than linear search,
    but only works for sorted lists!

    Parameters
    ----------
    search_list : list
        list to be searched
    item : any
        item we are looking for
    start : int
        start position for search range
    end : int
        end position for search range

    Returns
    -------
    int or False

    Examples
    --------
    >>> binary_search([0,1,7,9], 7)
    2

    >>> binary_search([0,1,7,9], 8)
    False

    >>> binary_search([0,1,7,9], 7, start=0, end=1)
    False
    """
    # First some safety checks
    # ========================

    # instantiate default value for end
    if end is None:
        end = len(search_list) - 1

    # make sure the range is sane
    assert start >= 0, "Start value too low: {}".format(start)
    assert end < len(search_list), \
        "End value is {}, but cannot be higher than {}".format(end, len(search_list) - 1)

    # Now the actual algorithm
    # ========================

    # if the end is before the start, the list does not contain the item
    if end < start:
        return False

    # find middle of the current range
    middle = int(start + (end - start)/2)

    # Case 1: our item is to the left of the item at the midpoint
    if item < search_list[middle]:
        return binary_search(search_list, item, start, middle - 1)
    # Case 2: our item is to the right of the item at the midpoint
    elif item > search_list[middle]:
        return binary_search(search_list, item, middle + 1, end)
    # Case 3: we found our item, return its index
    elif item == search_list[middle]:
        return middle


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
