"""
Problem: Word Search II (LC 212) | Day 40 | Hard
Topic: Trie + Backtracking

Given an m x n board of characters and a list of words, return all words
that can be found in the board.

Each word must be constructed from letters of sequentially adjacent cells
(horizontally or vertically neighboring). The same cell may not be used
more than once in a word.

Example 1:
  Input:
    board = [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
  Output: ["eat","oath"]

Example 2:
  Input:
    board = [["a","b"],
             ["c","d"]]
    words = ["abcb"]
  Output: []

Constraints:
  - m == board.length, n == board[i].length
  - 1 <= m, n <= 12
  - board[i][j] is a lowercase English letter
  - 1 <= words.length <= 3 * 10^4
  - 1 <= words[i].length <= 10
  - words[i] consists of lowercase English letters
  - All strings in words are unique

Hint: Build a trie from the word list. For each cell in the board, start
      a DFS that follows the trie. When is_end is True, add the word to
      results. Mark visited cells to avoid reuse. Prune trie nodes after
      finding words to optimize.
Pattern: Trie + Backtracking
"""

from typing import List


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class Solution:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


# --- Tests ---
if __name__ == "__main__":
    sol = Solution()

    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    result1 = sol.find_words(board1, ["oath", "pea", "eat", "rain"])
    assert sorted(result1) == sorted(["eat", "oath"])

    board2 = [["a", "b"], ["c", "d"]]
    result2 = sol.find_words(board2, ["abcb"])
    assert result2 == []

    board3 = [["a"]]
    result3 = sol.find_words(board3, ["a"])
    assert result3 == ["a"]

    board4 = [["a", "a"]]
    result4 = sol.find_words(board4, ["aaa"])
    assert result4 == []

    print("All tests passed!")
