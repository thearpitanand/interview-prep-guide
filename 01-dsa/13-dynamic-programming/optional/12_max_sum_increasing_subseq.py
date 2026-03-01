"""
Problem: Maximum Sum Increasing Subsequence (GFG) | Optional | Medium
Topic: Dynamic Programming

Find the maximum sum of an increasing subsequence.

Example 1:
  Input: arr = [1, 101, 2, 3, 100, 4, 5]
  Output: 106  # [1, 2, 3, 100]

Constraints:
  - 1 <= n <= 10^3

Hint: Like LIS, but dp[i] = max sum ending at i instead of length.
Pattern: DP (LIS variant)
"""


def max_sum_increasing_subseq(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5]) == 106
    assert max_sum_increasing_subseq([3, 4, 5, 10]) == 22
    print("All tests passed!")
