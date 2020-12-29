"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import fileinput
from pathlib import Path
from typing import Callable, Optional


def default_tokenizer(input_data):
    yield input_data


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    filtered_files = (
        file for file in dir_path.iterdir() if file.suffix[1:] == file_extension
    )
    tokenizer = tokenizer or default_tokenizer

    amount_of_tokens = 0
    with fileinput.input(filtered_files) as data:
        for token in map(tokenizer, data):
            amount_of_tokens += sum(1 for _ in token)
        return amount_of_tokens
