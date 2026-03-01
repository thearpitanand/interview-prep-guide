"""
Exercise: Loops | Day 1
Topic: Python Basics

Practice for loops, while loops, range, and loop patterns.

Instructions: Implement each function below.
"""


def sum_range(n: int) -> int:
    """Return sum of numbers from 1 to n (inclusive) using a loop."""
    pass


def factorial(n: int) -> int:
    """Return n! using a loop. 0! = 1."""
    pass


def reverse_string(s: str) -> str:
    """Reverse a string using a loop (don't use s[::-1])."""
    pass


def count_vowels(s: str) -> int:
    """Count the number of vowels (a, e, i, o, u) in s.
    Case-insensitive.
    """
    pass


def fibonacci(n: int) -> list[int]:
    """Return first n Fibonacci numbers.
    Example: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert sum_range(5) == 15
    assert sum_range(10) == 55

    assert factorial(5) == 120
    assert factorial(0) == 1

    assert reverse_string("hello") == "olleh"
    assert reverse_string("a") == "a"

    assert count_vowels("Hello World") == 3
    assert count_vowels("rhythm") == 0

    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(1) == [0]
    print("All tests passed!")
