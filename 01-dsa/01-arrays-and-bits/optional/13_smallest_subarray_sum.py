"""
Problem: Smallest Subarray with Sum > X (LC 209) | Optional | Medium
Topic: Arrays

Given an array of positive integers and a value X, find the length of the
smallest contiguous subarray whose sum is greater than X. Return 0 if none.

Example 1:
  Input: arr = [1, 4, 45, 6, 0, 19], x = 51
  Output: 3  # [4, 45, 6]

Constraints:
  - 1 <= n <= 10^5
  - 1 <= arr[i] <= 10^4

Hint: Sliding window — expand right, shrink left while sum > x.
Pattern: Sliding Window
"""


def smallest_subarray_sum(arr: list[int], x: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert smallest_subarray_sum([1, 4, 45, 6, 0, 19], 51) == 3
    assert smallest_subarray_sum([1, 10, 5, 2, 7], 9) == 1
    assert smallest_subarray_sum([1, 2, 3], 100) == 0
    print("All tests passed!")
