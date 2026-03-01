"""
Problem: Count All Palindromic Subsequences (GFG) | Optional | Hard
Topic: Dynamic Programming

Count all distinct palindromic subsequences in a string.

Example 1:
  Input: s = "abcd"
  Output: 4  # a, b, c, d

Constraints:
  - 1 <= len(s) <= 10^3

Hint: dp[i][j] = count of palindromic subsequences in s[i..j].
Pattern: Interval DP
"""


def count_palindromic_subseq(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_palindromic_subseq("abcd") == 4
    assert count_palindromic_subseq("aab") == 4
    print("All tests passed!")
