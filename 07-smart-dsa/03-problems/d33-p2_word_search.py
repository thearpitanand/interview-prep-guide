"""
Problem: Word Search (LC 79) | Smart-DSA Day 33 | Medium
Pattern: Backtracking (DFS on grid)
Time target: 30 minutes

Given an m x n grid of characters board and a string word, return True if
the word exists in the grid. The word can be constructed from letters of
sequentially adjacent cells (horizontally or vertically). The same cell may
not be used more than once.

Example 1:
  Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         word = "ABCCED"
  Output: True

Example 2:
  Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         word = "SEE"
  Output: True

Example 3:
  Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         word = "ABCB"
  Output: False

Constraints:
  - m == board.length, n == board[i].length
  - 1 <= m, n <= 6
  - 1 <= word.length <= 15
  - board and word consist of only lowercase and uppercase English letters.

Hint (⚠ read only after time budget is blown):
  DFS from every starting cell. Mark a cell as visited by replacing it with a
  sentinel (e.g. '#'). Restore it after the recursive call (backtrack).
  Return True as soon as the full word is matched.
"""


def exist(board: list[list[str]], word: str) -> bool:
    pass


if __name__ == "__main__":
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board1, "ABCCED") is True
    assert exist(board1, "SEE") is True
    assert exist(board1, "ABCB") is False

    board2 = [["a"]]
    assert exist(board2, "a") is True
    assert exist(board2, "b") is False
    print("All tests passed!")
