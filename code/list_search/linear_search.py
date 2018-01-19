#!/usr/bin/env python
# encoding: utf-8


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
        if search_item == search_list[i]:
            return i
    return False
