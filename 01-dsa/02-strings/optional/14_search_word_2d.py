"""
Problem: Search Word in 2D Grid (GFG) | Optional | Medium
Topic: Strings

Given a 2D grid and a word, check if the word exists in the grid. The word
can be constructed from horizontally or vertically adjacent cells (8 directions).

Example 1:
  Input: grid = [['G','E','E','K','S'],['F','O','R','G','E']], word = "GEEKS"
  Output: True

Constraints:
  - 1 <= R, C <= 50

Hint: DFS from each cell matching first character.
Pattern: DFS / Grid Search
"""


def search_word_2d(grid: list[list[str]], word: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    grid = [['G','E','E','K','S'],['F','O','R','G','E']]
    assert search_word_2d(grid, "GEEKS") == True
    assert search_word_2d(grid, "XYZ") == False
    print("All tests passed!")
