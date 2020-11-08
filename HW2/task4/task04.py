"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import Callable


def cache(func: Callable) -> Callable:
    d_cacher = {}

    def func_cache(*args):
        if args not in d_cacher:
            value = func(*args)
            d_cacher[args] = value
            return value
        else:
            return d_cacher[args]

    return func_cache
