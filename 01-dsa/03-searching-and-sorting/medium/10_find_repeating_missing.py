"""
Problem: Find Repeating and Missing Element (GFG) | Day 13 | Medium
Topic: Searching and Sorting

Given an unsorted array of size n with values from 1 to n. One number is
repeated and one is missing. Find both.

Example 1:
  Input: arr = [3, 1, 3]
  Output: (3, 2)  # 3 is repeating, 2 is missing

Constraints:
  - 2 <= n <= 10^5
  - 1 <= arr[i] <= n

Hint: Use XOR method or math (sum and sum of squares).
Pattern: Math / XOR
"""


def find_repeating_missing(arr: list[int]) -> tuple[int, int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_repeating_missing([3, 1, 3]) == (3, 2)
    assert find_repeating_missing([1, 1]) == (1, 2)
    assert find_repeating_missing([4, 3, 6, 2, 1, 1]) == (1, 5)
    print("All tests passed!")
