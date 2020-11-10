"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import defaultdict
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    ab, cd = defaultdict(int), defaultdict(int)
    len_lists = len(a)
    for i in range(len_lists):
        for j in range(len_lists):
            ab[a[i] + b[j]] += 1
            cd[c[i] + d[j]] += 1
    max_four = 0
    for key, val in ab.items():
        if -key in cd:
            max_four += max(val, cd[-key])
    return max_four
