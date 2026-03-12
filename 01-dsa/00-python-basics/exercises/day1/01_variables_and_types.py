"""
Exercise: Variables and Types | Day 1
Topic: Python Basics

Practice creating variables, understanding types,
and type conversion.

Instructions: Implement each function below.
"""


def get_type_name(value) -> str:
    """Return the type name of the value as a string.
    Example: get_type_name(42) -> 'int'
    """
    return type(value).__name__


def swap_values(a, b) -> tuple:
    """Return a tuple with values swapped.
    Example: swap_values(1, 2) -> (2, 1)
    """
    a, b = b, a
    return a, b


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.
    Formula: F = C * 9/5 + 32
    """
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def string_to_int_sum(a: str, b: str) -> int:
    """Convert two string numbers and return their sum.
    Example: string_to_int_sum("3", "4") -> 7
    """
    return int(a) + int(b)


# --- Tests ---
if __name__ == "__main__":
    assert get_type_name(42) == "int"
    assert get_type_name("hello") == "str"
    assert get_type_name(3.14) == "float"
    assert get_type_name(True) == "bool"

    assert swap_values(1, 2) == (2, 1)
    assert swap_values("a", "b") == ("b", "a")

    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

    assert is_even(4) == True
    assert is_even(7) == False

    assert string_to_int_sum("3", "4") == 7
    print("All tests passed!")
