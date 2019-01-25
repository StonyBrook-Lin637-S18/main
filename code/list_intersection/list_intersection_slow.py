#!/usr/bin/env python
# encoding: utf-8


def list_intersection(listA, listB):
    """Build a list that only contains elements of both lists.

    This algorithm is highly ineffecient
    because it loops over the second list multiple times!

    Parameters
    ----------
    listA : list
        first list of elements
    listB : list
        second list of elements

    Returns
    -------
    list

    Examples
    --------
    >>> list_intersection([3, 1, 2], [4, 7, 2, 1])
    [1, 2]

    >>> list_intersection([3, 1, 2], [])
    []

    >>> list_intersection([3, 1, 2], [1, 2, 3])
    [3, 1, 2]
    """
    # create empty intersection
    intersection = []

    # for each item a of listA
    for a in listA:
        # is any b of listB the same as a? 
        for b in listB:
            if a == b:
                # found a, add it to intersection
                intersection.append(a)

    # all loops done, return intersection
    return intersection
