from functools import wraps
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    """Декоратор автоматически логирует начало и конец выполнения функции"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: list, **kwargs: dict) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = "my_function ok\n"
            except Exception as e:
                result = None
                log_message = f"my_function error: {e}. Inputs: {args}, {kwargs} \n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return wrapper

    return decorator
