"""
Problem: Word Wrap Problem (GFG) | Optional | Hard
Topic: Strings

Given an array of word lengths and a line width, arrange words such that
total cost (sum of squares of extra spaces at end of each line) is minimized.

Example 1:
  Input: words = [3, 2, 2, 5], width = 6
  Output: minimum cost arrangement

Constraints:
  - 1 <= n <= 500
  - 1 <= word_len <= width

Hint: DP — cost[i] = min cost to arrange words[i..n-1].
Pattern: Dynamic Programming
"""


def word_wrap(words: list[int], width: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert word_wrap([3, 2, 2, 5], 6) == 10  # varies by formulation
    print("All tests passed!")
