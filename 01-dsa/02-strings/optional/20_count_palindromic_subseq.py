"""
Problem: Count All Palindromic Subsequences (GFG) | Optional | Hard
Topic: Strings

Given a string, count all distinct palindromic subsequences.

Example 1:
  Input: s = "abcd"
  Output: 4  # a, b, c, d

Example 2:
  Input: s = "aab"
  Output: 4  # a, b, aa, aab is not palindromic → a, a, b, aa

Constraints:
  - 1 <= len(s) <= 10^3

Hint: DP on intervals dp[i][j] = count of palindromic subsequences in s[i..j].
Pattern: Dynamic Programming
"""


def count_palindromic_subseq(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_palindromic_subseq("abcd") == 4
    assert count_palindromic_subseq("aab") == 4
    print("All tests passed!")
