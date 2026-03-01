"""
N-Queens (LC 51)

Day: 32 | Difficulty: Hard | Pattern: Backtracking - Constraint Satisfaction

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other. Given an integer n, return all
distinct solutions to the n-queens puzzle. You may return the answer in any
order.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.

Examples:
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There are exactly 2 distinct solutions for 4-queens.

    Input: n = 1
    Output: [["Q"]]

Constraints:
    - 1 <= n <= 9

Hint:
    Place queens row by row. For each row, try each column. Use three sets to
    track occupied columns, main diagonals (row - col), and anti-diagonals
    (row + col). If a column and both diagonals are free, place the queen and
    recurse to the next row. Backtrack by removing the queen.

Pattern: Backtracking with constraint sets. Place one queen per row, use sets
for O(1) conflict detection on columns and diagonals.
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """Return all valid N-Queens board configurations."""
    pass


def total_n_queens(n: int) -> int:
    """Return just the count of valid solutions (LC 52)."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: n = 4 has exactly 2 solutions
    result = solve_n_queens(4)
    assert len(result) == 2, f"Expected 2 solutions for n=4, got {len(result)}"

    # Test 2: Verify actual board configurations for n=4
    expected_boards = [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."]
    ]
    result_sorted = sorted([tuple(b) for b in result])
    expected_sorted = sorted([tuple(b) for b in expected_boards])
    assert result_sorted == expected_sorted, f"Board mismatch for n=4"

    # Test 3: n = 1
    result = solve_n_queens(1)
    assert result == [["Q"]], f"Expected [['Q']], got {result}"

    # Test 4: n = 8 has 92 solutions
    result = solve_n_queens(8)
    assert len(result) == 92, f"Expected 92 solutions for n=8, got {len(result)}"

    # Test 5: Validate no conflicts in each solution
    for board in solve_n_queens(5):
        queens = []
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == "Q":
                    queens.append((r, c))
        # Check no two queens share column or diagonal
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                r1, c1 = queens[i]
                r2, c2 = queens[j]
                assert c1 != c2, f"Column conflict: {queens[i]} and {queens[j]}"
                assert abs(r1 - r2) != abs(c1 - c2), f"Diagonal conflict: {queens[i]} and {queens[j]}"

    # Test 6: Count-only version
    assert total_n_queens(4) == 2, f"Expected 2, got {total_n_queens(4)}"
    assert total_n_queens(8) == 92, f"Expected 92, got {total_n_queens(8)}"

    print("All tests passed!")
