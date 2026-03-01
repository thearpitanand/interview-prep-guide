"""
Problem: Max Subsequence Sum No 3 Consecutive (GFG) | Optional | Medium
Topic: Dynamic Programming

Find the maximum sum of a subsequence such that no 3 elements are consecutive.

Example 1:
  Input: arr = [100, 1000, 100, 1000, 1]
  Output: 2101  # take all except the last

Constraints:
  - 1 <= n <= 10^5

Hint: dp[i] = max sum using arr[0..i] with no 3 consecutive. Consider including 0, 1, or 2 of the last elements.
Pattern: DP
"""


def max_sum_no_3_consecutive(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_sum_no_3_consecutive([100, 1000, 100, 1000, 1]) == 2101
    assert max_sum_no_3_consecutive([1, 2, 3]) == 5
    print("All tests passed!")
