"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import defaultdict
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    my_counter = defaultdict(int)
    for i in inp:
        my_counter[i] += 1
    major = sorted(my_counter.items(), key=lambda k: (k[1], k[0]))[-1][0]
    minor = sorted(my_counter.items(), key=lambda k: (k[1], k[0]))[0][0]
    return major, minor
