from functools import wraps
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    """Декоратор автоматически логирует начало и конец выполнения функции"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_messege = "my_function ok\n"
            except Exception as e:
                result = None
                log_messege = f"my_function error: {e}. Inputs: {args}, {kwargs} \n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_messege)
            else:
                print(log_messege)
            return result

        return wrapper

    return decorator
