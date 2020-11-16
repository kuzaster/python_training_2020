from unittest import mock

import pytest
from task02 import count_dots_on_i


def test_count_dots_on_i_unreal_site_by_mocking():
    with mock.patch("urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.side_effect = ValueError
        with pytest.raises(ValueError):
            count_dots_on_i("https://example.com/")


class FakeResponse:
    def __init__(self, *args, **kwargs):
        pass

    def read(self):
        return b"the only i"

    def decode(self):
        return "the only i"


def fake_urlopen(*args, **kwargs):
    return FakeResponse()


def test_count_dots_on_i_real_site_by_mocking():
    with mock.patch("urllib.request.urlopen", new=fake_urlopen):
        res = count_dots_on_i("https://example.com/")
        assert res == 1
