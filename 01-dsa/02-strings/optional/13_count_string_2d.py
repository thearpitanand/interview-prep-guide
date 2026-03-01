"""
Problem: Count String in 2D Character Array (GFG) | Optional | Medium
Topic: Strings

Given a 2D grid of characters and a word, count how many times the word
appears in all 8 directions.

Example 1:
  Input: grid = [['a','b','c'],['d','e','f'],['g','h','i']], word = "abc"
  Output: 1

Constraints:
  - 1 <= R, C <= 50
  - 1 <= len(word) <= R*C

Hint: From each cell, try all 8 directions.
Pattern: Grid Traversal
"""


def count_word_2d(grid: list[list[str]], word: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    grid = [['a','b','c'],['d','e','f'],['g','h','i']]
    assert count_word_2d(grid, "abc") == 1
    assert count_word_2d(grid, "z") == 0
    print("All tests passed!")
