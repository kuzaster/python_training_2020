import tempfile

import pytest
from task01 import KeyValueStorage


def with_temp_file(content):
    def create_temp_file(func):
        def replacement_function(*args, **kwargs):
            with tempfile.NamedTemporaryFile(mode="w+t") as data_file:
                data_file.write(content)
                data_file.flush()
                return func(data_file.name, *args, **kwargs)

        return replacement_function

    return create_temp_file


@with_temp_file(content="name=lol kek=cheb\npower=9001\n")
def test_keys_and_values_accessible_as_attributes(file_path):
    storage = KeyValueStorage(file_path)
    assert storage.name == "lol kek=cheb"
    assert storage.power == 9001


@with_temp_file(content="name=lol kek=cheb\npower=9001\n")
def test_keys_and_values_accessible_as_collection(file_path):
    storage = KeyValueStorage(file_path)
    assert storage["name"] == "lol kek=cheb"
    assert storage["power"] == 9001


@with_temp_file(content="name=kek\n1=first\n")
def test_with_unacceptable_type_of_key_for_attribute(file_path):
    with pytest.raises(ValueError):
        storage = KeyValueStorage(file_path)
