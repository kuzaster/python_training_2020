import urllib
from unittest import mock
from unittest.mock import MagicMock, Mock
from urllib import request

import pytest
from task02 import count_dots_on_i


def test_count_dots_on_i_real_site():
    with pytest.raises(ValueError):
        count_dots_on_i("https://example.com/user")


# def test_count_dots_on_i_mock_data():
#     with mock.patch("urllib.request.urlopen") as mock_urlopen:
#         a = Mock()
#         a.read.side_effect = 'i\n'
#         # a.decode.side_effect = 'i\n'
#         mock_urlopen.return_value = a
#         res = count_dots_on_i('https://example.com/')
#         assert res == 1
