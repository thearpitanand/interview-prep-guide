"""
Problem: Minimum Cost to Cut a Stick
Day: 30 | Difficulty: Hard | Topic: Greedy / DP
Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

Description:
    Given a wooden stick of length n units. The stick is labelled from 0 to n.
    Given an integer array cuts where cuts[i] denotes a position you should
    perform a cut at. The cost of one cut is the length of the stick to be cut.
    The total cost is the sum of costs of all cuts. When you cut a stick, it
    will be split into two smaller sticks (the sum of their lengths is the
    length of the stick before the cut).
    Return the minimum total cost of the cuts. The order of cuts can be changed
    as you wish.

Examples:
    Input: n = 7, cuts = [1, 3, 4, 5]
    Output: 16
    Explanation: Order [3, 5, 1, 4] gives cost 7 + 4 + 3 + 2 = 16.

    Input: n = 9, cuts = [5, 6, 1, 4, 2]
    Output: 22

Constraints:
    - 2 <= n <= 10^6
    - 1 <= cuts.length <= min(n - 1, 100)
    - 1 <= cuts[i] <= n - 1
    - All integers in cuts are distinct

Hint:
    This problem is best solved with interval DP (not pure greedy), but it
    appears in greedy sections because the cost depends on the order of cuts
    (a greedy-like intuition). Sort cuts, add 0 and n as boundaries.
    dp[i][j] = min cost to cut the segment between cuts[i] and cuts[j].
    For each pair (i, j), try every cut k between them:
    dp[i][j] = min(dp[i][k] + dp[k][j]) + (cuts[j] - cuts[i])

Pattern: Interval DP with greedy intuition. Sort cuts, add boundaries.
    For each subproblem (segment), try all possible first cuts and take minimum.
"""

from typing import List


def min_cost(n: int, cuts: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"n": 7, "cuts": [1, 3, 4, 5], "expected": 16},
        {"n": 9, "cuts": [5, 6, 1, 4, 2], "expected": 22},
        {"n": 4, "cuts": [2], "expected": 4},
        {"n": 10, "cuts": [2, 4, 7], "expected": 20},
        {"n": 5, "cuts": [1, 2, 3, 4], "expected": 12},
    ]

    for i, t in enumerate(tests):
        result = min_cost(t["n"], t["cuts"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
