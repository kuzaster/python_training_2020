from task03 import universal_file_counter
from tests.creation_temp_dir import with_temp_dir


@with_temp_dir(content_1="1\n3\n5\n", content_2="2\n4\n6\n", extension=".myexten")
def test_universal_file_counter_without_tokenizer(dir_path, extension):

    assert universal_file_counter(dir_path, extension) == 6


@with_temp_dir(content_1="1\n3\n5\n", content_2="2\n4\n6 7\n", extension=".myexten")
def test_universal_file_counter_with_tokenizer(dir_path, extension):

    assert universal_file_counter(dir_path, extension, str.split) == 7
