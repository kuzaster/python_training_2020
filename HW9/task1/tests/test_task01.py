from task01 import merge_sorted_files
from tests.creation_temp_files import with_three_temp_files, with_two_temp_files


@with_two_temp_files(content_1="1\n3\n5\n", content_2="2\n4\n6\n")
def test_merge_sorted_files_with_the_same_lengths(files_path):
    storage = tuple(merge_sorted_files(files_path))
    assert storage == (1, 2, 3, 4, 5, 6)


@with_two_temp_files(content_1="1\n3\n5\n7\n", content_2="2\n4\n")
def test_merge_sorted_files_with_first_file_longer_than_second(files_path):
    storage = tuple(merge_sorted_files(files_path))
    assert storage == (1, 2, 3, 4, 5, 7)


@with_two_temp_files(content_1="2\n4\n", content_2="1\n3\n5\n7\n")
def test_merge_sorted_files_with_second_file_longer_than_first(files_path):
    storage = tuple(merge_sorted_files(files_path))
    assert storage == (1, 2, 3, 4, 5, 7)


@with_two_temp_files(content_1="1\n3\n5\n", content_2="20\n40\n60\n")
def test_merge_sorted_files_with_data_in_first_file_smaller_than_in_second(files_path):
    storage = tuple(merge_sorted_files(files_path))
    assert storage == (1, 3, 5, 20, 40, 60)


@with_three_temp_files(
    content_1="1\n3\n5\n", content_2="2\n4\n8\n", content_3="6\n7\n9\n"
)
def test_merge_sorted_files_with_three_files(files_path):
    storage = tuple(merge_sorted_files(files_path))
    assert storage == (1, 2, 3, 4, 5, 6, 7, 8, 9)
