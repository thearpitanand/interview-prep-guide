"""
Problem: Matrix Chain Multiplication
Day: 39 | Difficulty: Medium | Topic: Interval DP
Link: Classic DP problem (no LeetCode link)

Description:
    Given a sequence of matrices, find the most efficient way to multiply
    these matrices together. The problem is not actually to perform the
    multiplications, but merely to decide in which order to perform them.
    Given dimensions array p where matrix i has dimensions p[i-1] x p[i],
    find the minimum number of scalar multiplications needed.

Examples:
    Input: p = [40, 20, 30, 10, 30]
    Output: 26000
    Explanation: Matrices A(40x20), B(20x30), C(30x10), D(10x30).
    Optimal: (A(BC))D = 20*30*10 + 40*20*10 + 40*10*30 = 6000+8000+12000 = 26000

    Input: p = [10, 20, 30]
    Output: 6000
    Explanation: Only one way: A(10x20) * B(20x30) = 10*20*30 = 6000.

Constraints:
    - 2 <= len(p) <= 100
    - 1 <= p[i] <= 500

Hint:
    dp[i][j] = minimum multiplications to compute the product of matrices
    i through j. Try all split points k (i <= k < j):
    dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]) for all k.
    Base case: dp[i][i] = 0 (single matrix needs no multiplication).
    Fill by increasing chain length.

Pattern: Interval DP. The key is trying every possible split point to divide
    the chain into two halves. Fill table by interval length from 2 to n.
"""

from typing import List


def matrix_chain_order(p: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"p": [40, 20, 30, 10, 30], "expected": 26000},
        {"p": [10, 20, 30], "expected": 6000},
        {"p": [10, 30, 5, 60], "expected": 4500},
        {"p": [1, 2, 3, 4], "expected": 18},
        {"p": [10, 20], "expected": 0},
        {"p": [5, 10, 3, 12, 5, 50, 6], "expected": 2010},
    ]

    for i, t in enumerate(tests):
        result = matrix_chain_order(t["p"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
