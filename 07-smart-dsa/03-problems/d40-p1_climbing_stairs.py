"""
Problem: Climbing Stairs (LC 70) | Smart-DSA Day 40 | Easy
Pattern: 1D Dynamic Programming
Time target: 15 minutes

You are climbing a staircase that takes n steps to reach the top. Each time
you can either climb 1 or 2 steps. In how many distinct ways can you climb
to the top?

Example 1:
  Input: n = 2
  Output: 2
  Explanation: (1+1) or (2)

Example 2:
  Input: n = 3
  Output: 3
  Explanation: (1+1+1), (1+2), or (2+1)

Constraints:
  - 1 <= n <= 45

Hint (⚠ read only after time budget is blown):
  dp[i] = dp[i-1] + dp[i-2]. This is Fibonacci. You only need two variables —
  no array needed.
"""


def climb_stairs(n: int) -> int:
    pass


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    print("All tests passed!")
