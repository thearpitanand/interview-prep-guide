"""
Problem: Maximal Rectangle
LeetCode: 85 - https://leetcode.com/problems/maximal-rectangle/
Day: 16
Difficulty: Hard
Topic: Stack/Histogram

Description:
    Given a rows x cols binary matrix filled with 0's and 1's, find
    the largest rectangle containing only 1's and return its area.

Examples:
    Input: matrix = [["1","0","1","0","0"],
                     ["1","0","1","1","1"],
                     ["1","1","1","1","1"],
                     ["1","0","0","1","0"]]
    Output: 6
    Explanation: The maximal rectangle is shown in rows 1-2, cols 2-4.

    Input: matrix = [["0"]]
    Output: 0

    Input: matrix = [["1"]]
    Output: 1

Constraints:
    - rows == matrix.length
    - cols == matrix[i].length
    - 1 <= rows, cols <= 200
    - matrix[i][j] is '0' or '1'

Hint:
    Build on "Largest Rectangle in Histogram" (LC 84).
    For each row, compute a histogram where heights[j] = number of
    consecutive 1's above (including current row) in column j. If
    current cell is '0', height resets to 0. Then find the largest
    rectangle in that histogram using a monotonic stack.

Pattern: Stack/Histogram
    - Build heights array row by row:
      heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
    - For each row, apply "largest rectangle in histogram" algorithm
    - Histogram algorithm uses a monotonic stack:
      - Push indices of increasing heights
      - On a shorter bar, pop and calculate area with popped height
      - Width = current_index - stack_top - 1
    - Time: O(rows * cols), Space: O(cols)
"""

from typing import List


def maximal_rectangle(matrix: List[List[str]]) -> int:
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: Standard case
    assert maximal_rectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]) == 6

    # Test 2: Single zero
    assert maximal_rectangle([["0"]]) == 0

    # Test 3: Single one
    assert maximal_rectangle([["1"]]) == 1

    # Test 4: Empty matrix
    assert maximal_rectangle([]) == 0

    # Test 5: All ones
    assert maximal_rectangle([
        ["1", "1"],
        ["1", "1"],
    ]) == 4

    # Test 6: Single row
    assert maximal_rectangle([["1", "0", "1", "1", "1"]]) == 3

    # Test 7: Single column
    assert maximal_rectangle([["1"], ["1"], ["0"], ["1"]]) == 2

    print("All test cases passed!")
