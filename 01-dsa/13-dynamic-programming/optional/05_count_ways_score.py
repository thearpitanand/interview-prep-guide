"""
Problem: Count Ways to Reach Nth Stair (GFG) | Optional | Easy
Topic: Dynamic Programming

Count ways to reach the nth stair if you can take 1, 2, or 3 steps.

Example 1:
  Input: n = 4
  Output: 7

Constraints:
  - 1 <= n <= 10^4

Hint: dp[i] = dp[i-1] + dp[i-2] + dp[i-3].
Pattern: DP
"""


def count_ways(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_ways(4) == 7
    assert count_ways(1) == 1
    assert count_ways(3) == 4
    print("All tests passed!")
