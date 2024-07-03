from unittest.mock import mock_open, patch
from src.decorators import log
from typing import Any


def test_log_terminal_ok(capsys: Any) -> None:
    @log()
    def exemple(x: list) -> Any:
        return x[0]

    exemple([1])
    capture = capsys.readouterr()
    assert capture.out == "my_function ok\n\n"


def test_log_terminal_error(capsys: Any) -> None:
    @log()
    def exemple_2(x: list) -> Any:
        return x[1]

    exemple_2([0])
    capture = capsys.readouterr()
    assert capture.out == "my_function error: list index out of range. Inputs: ([0],), {} \n\n"
