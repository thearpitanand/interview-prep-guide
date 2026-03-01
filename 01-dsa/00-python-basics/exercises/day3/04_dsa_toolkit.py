"""
Exercise: DSA Toolkit | Day 3
Topic: Python modules for DSA

Practice heapq, bisect, lru_cache, and itertools.

Instructions: Implement each function below.
"""

import heapq
import bisect
from functools import lru_cache
from itertools import permutations, combinations


def k_smallest(nums: list[int], k: int) -> list[int]:
    """Return k smallest elements using heapq.nsmallest.
    Example: k_smallest([3,1,4,1,5,9], 3) -> [1,1,3]
    """
    pass


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    """Merge multiple sorted lists into one sorted list.
    Use heapq.merge.
    """
    pass


def count_less_than(sorted_nums: list[int], target: int) -> int:
    """Count numbers strictly less than target in a sorted list.
    Use bisect_left. O(log n).
    """
    pass


def fibonacci_memo(n: int) -> int:
    """Return nth Fibonacci number using lru_cache.
    fib(0)=0, fib(1)=1
    """
    pass


def all_permutations(s: str) -> list[str]:
    """Return sorted list of all unique permutations of string.
    Example: all_permutations("ab") -> ["ab", "ba"]
    """
    pass


def all_combinations(nums: list[int], k: int) -> list[tuple]:
    """Return all combinations of k elements from nums.
    Example: all_combinations([1,2,3], 2) -> [(1,2),(1,3),(2,3)]
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert k_smallest([3, 1, 4, 1, 5, 9], 3) == [1, 1, 3]

    assert merge_sorted_lists([[1, 3, 5], [2, 4, 6]]) == [1, 2, 3, 4, 5, 6]

    assert count_less_than([1, 2, 3, 4, 5], 3) == 2
    assert count_less_than([1, 2, 3, 4, 5], 1) == 0

    assert fibonacci_memo(10) == 55
    assert fibonacci_memo(0) == 0

    assert all_permutations("ab") == ["ab", "ba"]

    assert all_combinations([1, 2, 3], 2) == [(1, 2), (1, 3), (2, 3)]
    print("All tests passed!")
