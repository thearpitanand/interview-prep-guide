"""
Problem: Edit Distance (LC 72) | Day 11 | Hard
Topic: Strings

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 into word2.

You have the following three operations permitted on a word:
  - Insert a character
  - Delete a character
  - Replace a character

Example 1:
  Input: word1 = "horse", word2 = "ros"
  Output: 3
  Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose  (remove 'r')
    rose  -> ros   (remove 'e')

Example 2:
  Input: word1 = "intention", word2 = "execution"
  Output: 5
  Explanation:
    intention -> inention  (remove 't')
    inention  -> enention  (replace 'i' with 'e')
    enention  -> exention  (replace 'n' with 'x')
    exention  -> exection  (replace 'n' with 'c')
    exection  -> execution (insert 'u')

Constraints:
  - 0 <= len(word1), len(word2) <= 500
  - word1 and word2 consist of lowercase English letters

Hint: Use a 2D DP table where dp[i][j] = min operations to convert
      word1[:i] to word2[:j].
      - If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] (no operation)
      - Else: dp[i][j] = 1 + min(dp[i-1][j],     # delete
                                   dp[i][j-1],     # insert
                                   dp[i-1][j-1])   # replace
      Base cases: dp[i][0] = i (delete all), dp[0][j] = j (insert all).
Pattern: Dynamic Programming
"""


def min_distance(word1: str, word2: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "") == 0
    assert min_distance("", "abc") == 3
    assert min_distance("abc", "") == 3
    assert min_distance("abc", "abc") == 0
    assert min_distance("a", "b") == 1
    print("All tests passed!")
