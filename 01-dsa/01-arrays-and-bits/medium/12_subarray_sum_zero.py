"""
Problem: Subarray with Sum 0 (GFG) | Day 5 | Medium
Topic: Arrays

Given an array of positive and negative numbers, find if there is a subarray
(of size at least one) with sum 0.

Example 1:
  Input: arr = [4, 2, -3, 1, 6]
  Output: True  # subarray [2, -3, 1] has sum 0

Example 2:
  Input: arr = [4, 2, 0, 1, 6]
  Output: True  # subarray [0] has sum 0

Constraints:
  - 1 <= n <= 10^4
  - -10^5 <= arr[i] <= 10^5

Hint: Track prefix sums — if a prefix sum repeats or equals 0, there's a zero-sum subarray.
Pattern: Prefix Sum + Hash Set
"""


def subarray_sum_zero(arr: list[int]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert subarray_sum_zero([4, 2, -3, 1, 6]) == True
    assert subarray_sum_zero([4, 2, 0, 1, 6]) == True
    assert subarray_sum_zero([1, 2, 3]) == False
    assert subarray_sum_zero([-1, 1]) == True
    print("All tests passed!")
