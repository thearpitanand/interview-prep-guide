"""
Problem: Word Search
LeetCode: 79 - https://leetcode.com/problems/word-search/
Day: 16
Difficulty: Medium
Topic: DFS/Backtracking

Description:
    Given an m x n grid of characters board and a string word, return
    true if word exists in the grid. The word can be constructed from
    letters of sequentially adjacent cells, where adjacent cells are
    horizontally or vertically neighboring. The same letter cell may
    not be used more than once.

Examples:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: True

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: True

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: False

Constraints:
    - m == board.length
    - n == board[i].length
    - 1 <= m, n <= 6
    - 1 <= word.length <= 15
    - board and word consist of only lowercase and uppercase English letters

Hint:
    Use DFS with backtracking. For each cell matching word[0], start
    a DFS. At each step, mark the cell as visited (e.g., replace with
    '#'), explore 4 neighbors for the next character, then restore the
    cell (backtrack). Return True if index reaches len(word).

Pattern: DFS/Backtracking on Grid
    - Try every cell as starting point
    - DFS tracks current index in word
    - Mark cell visited before recursing, restore after (backtrack)
    - Prune: if cell doesn't match current character, return False
    - Time: O(m * n * 4^L) where L = word length
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    # Test 1: Word exists with turns
    assert exist(board, "ABCCED") is True

    # Test 2: Word exists straight path
    assert exist(board, "SEE") is True

    # Test 3: Word requires revisiting a cell (should fail)
    assert exist(board, "ABCB") is False

    # Test 4: Single character found
    assert exist([["A"]], "A") is True

    # Test 5: Single character not found
    assert exist([["A"]], "B") is False

    # Test 6: Whole board is the word
    assert exist([["A", "B"], ["C", "D"]], "ABDC") is True

    print("All test cases passed!")
