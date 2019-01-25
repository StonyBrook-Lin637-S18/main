#!/usr/bin/env python
# encoding: utf-8


def list_intersection(listA, listB):
    """Build a list that only contains elements of all lists.

    This algorithm uses dictionaries for speed,
    but requires more memory.
    """
    # convert second list to dictionary
    dictB = {item: item for item in listB}

    # create empty intersection
    intersection = []

    # for each item a of listA
    for a in listA:
        # is a in listB?
        if dictB.get(a):
            # found a, add it to intersection
            intersection.append(a)

    # return intersection
    return intersection
