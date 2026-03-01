"""
Problem: LCS of 3 Strings (GFG) | Optional | Medium
Topic: Dynamic Programming

Find the longest common subsequence of three strings.

Example 1:
  Input: s1 = "geeks", s2 = "geeksfor", s3 = "geeksforgeeks"
  Output: 5  # "geeks"

Constraints:
  - 1 <= len(s1), len(s2), len(s3) <= 100

Hint: 3D DP: dp[i][j][k] extending standard LCS to 3 strings.
Pattern: 3D DP
"""


def lcs_three(s1: str, s2: str, s3: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert lcs_three("geeks", "geeksfor", "geeksforgeeks") == 5
    assert lcs_three("abcd", "efgh", "ijkl") == 0
    print("All tests passed!")
