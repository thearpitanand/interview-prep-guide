"""
Problem: Smallest Sum Contiguous Subarray (GFG) | Optional | Easy
Topic: Dynamic Programming

Find the contiguous subarray with the smallest (most negative) sum.

Example 1:
  Input: arr = [3, -4, 2, -3, -1, 7, -5]
  Output: -6  # subarray [-4, 2, -3, -1]

Constraints:
  - 1 <= n <= 10^5

Hint: Kadane's variant — track min instead of max.
Pattern: Kadane's Algorithm (Min variant)
"""


def smallest_sum_subarray(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert smallest_sum_subarray([3, -4, 2, -3, -1, 7, -5]) == -6
    assert smallest_sum_subarray([1, 2, 3]) == 1
    assert smallest_sum_subarray([-5]) == -5
    print("All tests passed!")
