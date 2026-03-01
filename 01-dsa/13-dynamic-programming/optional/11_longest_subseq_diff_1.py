"""
Problem: Longest Subsequence Adjacent Diff = 1 (GFG) | Optional | Medium
Topic: Dynamic Programming

Find the longest subsequence where absolute difference between adjacent
elements is 1.

Example 1:
  Input: arr = [1, 2, 3, 4, 5, 3, 2]
  Output: 6  # [1,2,3,4,3,2]

Constraints:
  - 1 <= n <= 10^5

Hint: dp[i] = longest subseq ending at i. For each i, check all j < i where |arr[i]-arr[j]| == 1.
Pattern: DP
"""


def longest_subseq_diff_1(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_subseq_diff_1([1, 2, 3, 4, 5, 3, 2]) == 6
    assert longest_subseq_diff_1([10, 9, 4, 5, 4, 8, 6]) == 3
    print("All tests passed!")
