"""
Exercise: Memoization & itertools | Day 5
Topic: functools.lru_cache and itertools

Practice memoization for recursive problems and itertools utilities.

Instructions: Implement each function below.
"""

from functools import lru_cache
from itertools import permutations, combinations, product, chain, groupby


def fibonacci_memo(n: int) -> int:
    """Return nth Fibonacci number using @lru_cache.
    fib(0)=0, fib(1)=1, fib(n) = fib(n-1) + fib(n-2)
    """
    pass


def climb_stairs(n: int) -> int:
    """Return number of ways to climb n stairs (1 or 2 steps at a time).
    Use @lru_cache for memoization.
    Example: climb_stairs(3) -> 3  (1+1+1, 1+2, 2+1)
    """
    pass


def flatten_lists(lists: list[list]) -> list:
    """Flatten a list of lists into a single list using chain.from_iterable().
    Example: flatten_lists([[1, 2], [3], [4, 5]]) -> [1, 2, 3, 4, 5]
    """
    pass


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first letter using itertools.groupby.
    Words must be sorted first (groupby only groups consecutive elements).
    Return a dict mapping first letter to list of words.
    Example: group_by_first_letter(["apple", "banana", "avocado", "blueberry"])
    -> {"a": ["apple", "avocado"], "b": ["banana", "blueberry"]}
    """
    pass


def all_binary_strings(n: int) -> list[str]:
    """Generate all binary strings of length n using itertools.product.
    Return sorted list of strings.
    Example: all_binary_strings(2) -> ["00", "01", "10", "11"]
    """
    pass


def generate_subsets(nums: list[int]) -> list[list[int]]:
    """Return all subsets of nums using itertools.combinations.
    Generate combinations of length 0, 1, 2, ..., len(nums).
    Sort by length, then lexicographically.
    Example: generate_subsets([1, 2]) -> [[], [1], [2], [1, 2]]
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert fibonacci_memo(10) == 55
    assert fibonacci_memo(0) == 0

    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8

    assert flatten_lists([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten_lists([[], [1]]) == [1]

    result = group_by_first_letter(["apple", "banana", "avocado", "blueberry"])
    assert result["a"] == ["apple", "avocado"]
    assert result["b"] == ["banana", "blueberry"]

    assert all_binary_strings(2) == ["00", "01", "10", "11"]
    assert all_binary_strings(1) == ["0", "1"]

    assert generate_subsets([1, 2]) == [[], [1], [2], [1, 2]]

    print("All tests passed!")
