from task03 import my_precious_logger


def test_my_precious_logger_stderr(capfd):
    my_precious_logger("error: file not found")
    out, err = capfd.readouterr()
    assert err == "error: file not found"


def test_my_precious_logger_stdout(capfd):
    my_precious_logger("OK")
    out, err = capfd.readouterr()
    assert out == "OK"
