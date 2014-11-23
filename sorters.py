#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sorts data."""


# import util

# print util.get_random(3)


def selection(iterable):
    """The algorithm proceeds by finding the smallest element in the
    unsorted sublist, exchanging it with the leftmost unsorted element
    (putting it in sorted order), and moving the sublist boundaries 
    one element to the right"""
    sortit = 0
    while sortit != len(iterable):
        for thevals in range(sortit, len(iterable)): 
            if iterable[thevals] < iterable[sortit]:
                iterable[sortit],iterable[thevals] = iterable[
                thevals],iterable[sortit]  
        sortit = sortit+1
    return iterable 

def quick(iterable):
    """Quicksort first divides a large array into two smaller sub-arrays: 
    the low elements and the high elements. 
    Quicksort can then recursively sort the sub-arrays"""
    smaller = []
    pivotlist = []
    bigger = []
    if len(iterable) <= 1:
        return iterable
    else:
        pivot = iterable[0]
        for theval in iterable:
            if theval < pivot:
                smaller.append(theval)
            elif theval > pivot:
                bigger.append(theval)
            else:
                pivotlist.append(theval)
        smaller = quick(smaller)
        bigger = quick(bigger)
        return smaller + pivotlist + bigger