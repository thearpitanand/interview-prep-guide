"""
Surrounded Regions (LC 130)

Day: 34 | Difficulty: Medium | Pattern: DFS from Boundary

Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'. A region is captured by flipping all
'O's into 'X's in that surrounded region.

An 'O' is NOT surrounded if it is on the border or connected to an 'O' on
the border.

Examples:
    Input: board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    Output: [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]
    Explanation: The bottom-left 'O' is on the border, so it's not captured.
                 The other O's are surrounded and get captured.

Constraints:
    - m == board.length
    - n == board[i].length
    - 1 <= m, n <= 200
    - board[i][j] is 'X' or 'O'

Hint:
    Instead of finding surrounded regions, find UN-surrounded regions first.
    Start DFS/BFS from all 'O's on the border. Mark these as safe (e.g., 'S').
    Then flip all remaining 'O's to 'X' (they're surrounded), and restore 'S'
    back to 'O'.

Pattern: Reverse thinking with boundary DFS - mark safe cells from boundaries,
then capture everything else.
"""

from collections import deque
from typing import List


def solve(board: List[List[str]]) -> None:
    """Modify board in-place: capture surrounded regions."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case with surrounded and border-connected O's
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solve(board)
    expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    assert board == expected, f"Expected {expected}, got {board}"

    # Test 2: All border O's (none captured)
    board = [
        ["O", "O"],
        ["O", "O"]
    ]
    solve(board)
    expected = [
        ["O", "O"],
        ["O", "O"]
    ]
    assert board == expected, f"Expected {expected}, got {board}"

    # Test 3: Single cell
    board = [["X"]]
    solve(board)
    assert board == [["X"]], f"Expected [['X']], got {board}"

    # Test 4: All X's (nothing to capture)
    board = [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"]
    ]
    solve(board)
    expected = [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"]
    ]
    assert board == expected, f"Expected {expected}, got {board}"

    # Test 5: Center O is fully surrounded
    board = [
        ["X", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"]
    ]
    solve(board)
    expected = [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"]
    ]
    assert board == expected, f"Expected {expected}, got {board}"

    print("All tests passed!")
