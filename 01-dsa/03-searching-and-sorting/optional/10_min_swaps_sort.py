"""
Problem: Min Swaps to Sort Array (GFG) | Optional | Medium
Topic: Searching and Sorting

Given an array, find the minimum number of swaps needed to sort it.

Example 1:
  Input: arr = [4, 3, 2, 1]
  Output: 2

Constraints:
  - 1 <= n <= 10^5

Hint: Build position graph, count cycles. Swaps = sum(cycle_length - 1).
Pattern: Graph Cycles
"""


def min_swaps_sort(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_swaps_sort([4, 3, 2, 1]) == 2
    assert min_swaps_sort([1, 5, 4, 3, 2]) == 2
    print("All tests passed!")
