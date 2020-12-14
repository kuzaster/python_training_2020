import tempfile
from pathlib import Path


def with_temp_dir(content_1, content_2, extension):
    def create_temp_dir(func):
        def replacement_function(*args, **kwargs):

            with tempfile.NamedTemporaryFile(
                mode="w+t", suffix=extension
            ) as file_1, tempfile.NamedTemporaryFile(
                mode="w+t", suffix=extension
            ) as file_2:
                temp = tempfile.gettempdir()

                file_1.write(content_1)
                file_1.flush()

                file_2.write(content_2)
                file_2.flush()

                return func(Path(temp), extension[1:], *args, **kwargs)

        return replacement_function

    return create_temp_dir
