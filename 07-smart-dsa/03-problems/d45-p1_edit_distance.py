"""
Problem: Edit Distance (LC 72) | Smart-DSA Day 45 | Hard
Pattern: Dynamic Programming — 2D String DP
Time target: 40 minutes

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 into word2. You have three operations:
  - Insert a character
  - Delete a character
  - Replace a character

Example 1:
  Input: word1 = "horse", word2 = "ros"
  Output: 3  (horse → rorse → rose → ros)

Example 2:
  Input: word1 = "intention", word2 = "execution"
  Output: 5

Constraints:
  - 0 <= word1.length, word2.length <= 500
  - word1 and word2 consist of lowercase English letters only.

Hint (⚠ read only after time budget is blown):
  dp[i][j] = min edits to convert word1[:i] to word2[:j].
  Base cases: dp[i][0] = i (delete all), dp[0][j] = j (insert all).
  If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] (free).
  Else: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
               (replace,             delete,       insert).
"""


def min_distance(word1: str, word2: str) -> int:
    pass


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "") == 0
    assert min_distance("a", "") == 1
    assert min_distance("", "b") == 1
    assert min_distance("abc", "abc") == 0
    print("All tests passed!")
