import urllib
from unittest import mock
from unittest.mock import MagicMock, Mock
from urllib import request

import pytest
from task02 import count_dots_on_i


def test_count_dots_on_i_real_site():
    assert count_dots_on_i("https://example.com/") == 59


def test_count_dots_on_i_unreal_site():
    with mock.patch("urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.side_effect = ValueError
        with pytest.raises(ValueError):
            count_dots_on_i("https://example.com/")


def test_count_dots_on_i_mock_data():
    with mock.patch("urllib.request.urlopen") as mock_urlopen:
        # a = MagicMock()
        # a.read.decode.side_effect = "ii\n"
        # mock_urlopen.return_value = a
        mock_urlopen.read.decode.return_value = "i\n"
        # mock_urlopen.read.decode.side_effect = "i\n"
        res = count_dots_on_i("https://example.com/")
        assert res == 1
