import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import List


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_sum_of_slow_calc(value: int) -> (int, int):
    pool = Pool(processes=30)
    values = [i for i in range(value + 1)]
    start = time.time()
    all_sum = sum(list(pool.map(slow_calculate, values)))
    finish = time.time()
    calc_time = finish - start
    return all_sum, calc_time
