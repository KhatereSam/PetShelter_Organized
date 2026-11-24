from functools import wraps
from datetime import datetime


def log_operation(function):
    """Print a short log message after a successful operation."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Operation completed: {function.__name__}")
        return result

    return wrapper
