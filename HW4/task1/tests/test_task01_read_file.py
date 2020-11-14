import os

import pytest
from task01_read_file import read_magic_number


@pytest.fixture
def clean_dir():
    creation_file = open("data.txt", "w")
    yield
    creation_file.close()
    os.remove("data.txt")


@pytest.mark.usefixtures("clean_dir")
@pytest.mark.parametrize(
    "value",
    [
        1,
        2,
        2.99,
    ],
)
def test_read_magic_number_is_true(value):
    with open("data.txt", "w") as f:
        f.write(f"{value}\n")
    path_file = os.path.join(os.path.dirname(__file__), "data.txt")
    assert read_magic_number(path_file) is True


@pytest.mark.usefixtures("clean_dir")
@pytest.mark.parametrize(
    "value",
    [
        0.99,
        3,
        5.2,
    ],
)
def test_read_magic_number_is_false(value):
    with open("data.txt", "w") as f:
        f.write(f"{value}\n")
    path_file = os.path.join(os.path.dirname(__file__), "data.txt")
    assert read_magic_number(path_file) is False


@pytest.mark.usefixtures("clean_dir")
def test_read_magic_number_is_value_error():
    with open("data.txt", "w") as f:
        f.write("a\n")
    path_file = os.path.join(os.path.dirname(__file__), "data.txt")
    with pytest.raises(ValueError):
        read_magic_number(path_file)


def test_read_magic_number_file_is_not_exist():
    assert read_magic_number("file_not_exist.txt") is None
