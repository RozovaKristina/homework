from unittest.mock import mock_open, patch
from src.decorators import log


def test_log_to_file_success():
    @log("test_log.txt")
    def my_function_1(x, y):
        return x + y

    with patch('builtins.open', mock_open()) as mocked_file:
        result = my_function_1(1, 2)
        assert result == 3
        mocked_file().write.assert_called_with("my_function ok\n")


def test_log_to_file_exception():
    @log("test_log.txt")
    def my_function_2(x, y):
        return x / y

    with patch('builtins.open', mock_open()) as mocked_file:
        result = my_function_2(1, 0)
        assert result is None
        assert any("division by zero" in call[0][0] for call in mocked_file().write.mock_calls)
