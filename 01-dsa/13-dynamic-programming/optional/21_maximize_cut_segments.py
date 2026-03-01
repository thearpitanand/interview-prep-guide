"""
Problem: Maximize Cut Segments (GFG) | Optional | Medium
Topic: Dynamic Programming

Given a rod of length N and three cut lengths a, b, c, maximize the number
of segments.

Example 1:
  Input: n = 7, a = 5, b = 2, c = 2
  Output: 2  # cuts of 5 and 2

Constraints:
  - 1 <= n <= 10^4

Hint: dp[i] = max segments for length i. dp[i] = max(dp[i-a], dp[i-b], dp[i-c]) + 1.
Pattern: DP (Unbounded)
"""


def maximize_cut_segments(n: int, a: int, b: int, c: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert maximize_cut_segments(7, 5, 2, 2) == 2
    assert maximize_cut_segments(4, 2, 1, 1) == 4
    print("All tests passed!")
