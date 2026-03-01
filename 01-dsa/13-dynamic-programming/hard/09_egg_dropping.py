"""
Problem: Egg Dropping Problem (LC 887) | Day 39 | Hard
Topic: Dynamic Programming

Given K eggs and N floors, find the minimum number of trials needed in the
worst case to find the critical floor.

Example 1:
  Input: k = 2, n = 10
  Output: 4

Constraints:
  - 1 <= k <= 100
  - 1 <= n <= 10^4

Hint: dp[k][n] = min trials with k eggs and n floors. Binary search optimization or dp[t][k] = max floors checkable with t trials and k eggs.
Pattern: DP with Binary Search / Optimized DP
"""


def egg_drop(k: int, n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert egg_drop(2, 10) == 4
    assert egg_drop(1, 10) == 10
    assert egg_drop(2, 6) == 3
    assert egg_drop(3, 14) == 4
    print("All tests passed!")
