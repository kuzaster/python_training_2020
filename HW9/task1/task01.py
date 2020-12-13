"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import Iterator, List, Union


def unpacking(files):
    for file in map(open, files):
        yield (int(data) for data in file)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    gen_data_files = (it for it in unpacking(file_list))
    # gen_data_files = (it for it in (map(int, data) for data in map(open, file_list))) # without function unpacking
    yield from heapq.merge(*gen_data_files)
