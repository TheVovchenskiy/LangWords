from typing import Any


def is_list_of_str(obj: Any) -> bool:
    """Checks if given obj is list of str's"""
    return isinstance(obj, list) and \
        all(isinstance(item, str) for item in obj)
