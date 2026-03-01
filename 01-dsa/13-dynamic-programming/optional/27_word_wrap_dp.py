"""
Problem: Word Wrap Problem DP (GFG) | Optional | Hard
Topic: Dynamic Programming

Given word lengths and line width, arrange words to minimize total cost
(sum of extra spaces squared).

Example 1:
  Input: words = [3, 2, 2, 5], width = 6
  Output: 10

Constraints:
  - 1 <= n <= 500

Hint: dp[i] = min cost to arrange words[i..n-1]. Try placing words[i..j] on one line.
Pattern: DP
"""


def word_wrap_dp(words: list[int], width: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert word_wrap_dp([3, 2, 2, 5], 6) == 10
    print("All tests passed!")
