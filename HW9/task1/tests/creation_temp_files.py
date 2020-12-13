import tempfile


def with_two_temp_files(content_1, content_2):
    def create_temp_file(func):
        def replacement_function(*args, **kwargs):
            with tempfile.NamedTemporaryFile(
                mode="w+t"
            ) as file_1, tempfile.NamedTemporaryFile(mode="w+t") as file_2:

                files_path = [file_1.name, file_2.name]

                file_1.write(content_1)
                file_1.flush()

                file_2.write(content_2)
                file_2.flush()

                return func(files_path, *args, **kwargs)

        return replacement_function

    return create_temp_file


def with_three_temp_files(content_1, content_2, content_3):
    def create_temp_file(func):
        def replacement_function(*args, **kwargs):
            with tempfile.NamedTemporaryFile(
                mode="w+t"
            ) as file_1, tempfile.NamedTemporaryFile(
                mode="w+t"
            ) as file_2, tempfile.NamedTemporaryFile(
                mode="w+t"
            ) as file_3:

                files_path = [file_1.name, file_2.name, file_3.name]

                file_1.write(content_1)
                file_1.flush()

                file_2.write(content_2)
                file_2.flush()

                file_3.write(content_3)
                file_3.flush()
                return func(files_path, *args, **kwargs)

        return replacement_function

    return create_temp_file
