"""
Sudoku Solver (LC 37)

Day: 32 | Difficulty: Hard | Pattern: Backtracking - Constraint Propagation

Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku
solution must satisfy all of the following rules:
    1. Each of the digits 1-9 must occur exactly once in each row.
    2. Each of the digits 1-9 must occur exactly once in each column.
    3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3
       sub-boxes of the grid.

The '.' character indicates empty cells.

Examples:
    Input: board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Output: board is filled in-place with the valid solution

Constraints:
    - board.length == 9
    - board[i].length == 9
    - board[i][j] is a digit or '.'
    - It is guaranteed that the input board has only one solution

Hint:
    Find the next empty cell, try digits 1-9. For each digit, check if it's
    valid (not in same row, column, or 3x3 box). If valid, place it and recurse.
    If recursion fails, remove the digit and try the next one. Use sets for
    rows, columns, and boxes for O(1) validation.

Pattern: Backtracking with constraint checking. Find empty cell -> try digits
-> validate -> recurse -> backtrack. Return True/False to signal success.
"""

from typing import List


def solve_sudoku(board: List[List[str]]) -> None:
    """Solve the sudoku puzzle in-place."""
    pass


def solve_sudoku_optimized(board: List[List[str]]) -> None:
    """Optimized: precompute row/col/box sets for O(1) validation."""
    pass


# --- Helper ---

def print_board(board: List[List[str]]) -> None:
    """Pretty print the sudoku board."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        line = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                line += "| "
            line += val + " "
        print(line)


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """Verify that a completed board is a valid sudoku solution."""
    for i in range(9):
        row = [board[i][j] for j in range(9) if board[i][j] != "."]
        col = [board[j][i] for j in range(9) if board[j][i] != "."]
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return False

    for box_r in range(3):
        for box_c in range(3):
            box = []
            for r in range(box_r * 3, box_r * 3 + 3):
                for c in range(box_c * 3, box_c * 3 + 3):
                    if board[r][c] != ".":
                        box.append(board[r][c])
            if len(box) != len(set(box)):
                return False

    return True


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard sudoku puzzle
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solve_sudoku(board)

    # Verify no empty cells remain
    for row in board:
        assert "." not in row, f"Found empty cell in solved board"

    # Verify solution is valid
    assert is_valid_sudoku(board), "Solution is not valid"

    # Verify specific cells
    assert board[0] == ["5", "3", "4", "6", "7", "8", "9", "1", "2"], \
        f"Row 0 mismatch: {board[0]}"

    # Test 2: Almost complete board
    board2 = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", ".", "7", "9"]
    ]
    solve_sudoku(board2)
    assert board2[8][6] == "1", f"Expected '1' at [8][6], got {board2[8][6]}"

    # Test 3: Optimized version
    board3 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solve_sudoku_optimized(board3)
    assert is_valid_sudoku(board3), "Optimized solution is not valid"

    print("All tests passed!")
