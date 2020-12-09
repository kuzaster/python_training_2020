"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
# >>> with suppressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            yield
        except self.exception:
            pass


@contextmanager
def suppressor(exception):
    try:
        try:
            yield
        finally:
            pass
    except exception:
        pass
