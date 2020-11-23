import os
import tempfile

import pytest
from task01_read_file import read_magic_number


def with_temp_file(content):
    def create_temp_file(func):
        def replacement_function(*args, **kwargs):
            with tempfile.NamedTemporaryFile(mode="w+t") as data_file:
                data_file.write(content)
                data_file.flush()
                return func(data_file.name, *args, **kwargs)

        return replacement_function

    return create_temp_file


@with_temp_file(content="2.99\n")
def test_read_magic_number_with_number_greater_or_equal_1_and_less_3(file_path):
    assert read_magic_number(file_path) is True


@with_temp_file(content="0.99\n")
def test_read_magic_number_with_number_less_1(file_path):
    assert read_magic_number(file_path) is False


@with_temp_file(content="3\n")
def test_read_magic_number_with_number_greater_or_equal_3(file_path):
    assert read_magic_number(file_path) is False


@with_temp_file(content="a\n")
def test_read_magic_number_with_string_in_data_file(file_path):
    with pytest.raises(ValueError):
        read_magic_number(file_path)


def test_read_magic_number_with_nonexistent_file():
    with pytest.raises(ValueError):
        read_magic_number("file_not_exist.txt")
