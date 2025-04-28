import os
import pytest
from src.decorators import log


@pytest.fixture
def log_file():
    filename = "test_log.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


def test_log_to_file(log_file):
    @log(filename=log_file)
    def add(a, b):
        return a + b

    add(1, 2)

    with open(log_file, "r") as f:
        content = f.read()
    assert "add ok" in content


def test_log_to_console(capsys):
    @log()
    def multiply(x, y):
        return x * y

    multiply(3, 4)
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_exception(log_file):
    @log(filename=log_file)
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    with open(log_file, "r") as f:
        content = f.read()
    assert "divide error: ZeroDivisionError" in content