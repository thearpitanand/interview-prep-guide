"""
Exercise: Functions | Day 2
Topic: Python Functions

Practice function definitions, args, kwargs, and lambdas.

Instructions: Implement each function below.
"""


def apply_operation(a: int, b: int, operation: str) -> float:
    """Apply the operation to a and b.
    Operations: 'add', 'subtract', 'multiply', 'divide'
    For divide, return float. Raise ValueError for unknown ops.
    """
    pass


def make_multiplier(factor: int):
    """Return a function that multiplies its input by factor.
    Example: double = make_multiplier(2); double(5) -> 10
    """
    pass


def apply_to_list(lst: list, func) -> list:
    """Apply func to each element and return new list.
    Don't use map().
    """
    pass


def compose(f, g):
    """Return a function that computes f(g(x)).
    Example: compose(str, abs)(-5) -> '5'
    """
    pass


def memoize(func):
    """Return a memoized version of func.
    Cache results for previously seen arguments.
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert apply_operation(3, 4, 'add') == 7
    assert apply_operation(10, 3, 'subtract') == 7
    assert apply_operation(3, 4, 'multiply') == 12
    assert apply_operation(10, 4, 'divide') == 2.5

    double = make_multiplier(2)
    assert double(5) == 10
    assert double(3) == 6

    assert apply_to_list([1, 2, 3], lambda x: x * 2) == [2, 4, 6]

    str_abs = compose(str, abs)
    assert str_abs(-5) == "5"

    call_count = 0
    def expensive(n):
        nonlocal call_count
        call_count += 1
        return n * n
    memo_expensive = memoize(expensive)
    assert memo_expensive(5) == 25
    assert memo_expensive(5) == 25
    assert call_count == 1  # Only called once
    print("All tests passed!")
