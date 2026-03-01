"""
Problem: Painting Fence Problem (GFG) | Optional | Medium
Topic: Dynamic Programming

Given n fence posts and k colors, count ways to paint such that no more
than 2 adjacent posts have the same color.

Example 1:
  Input: n = 3, k = 2
  Output: 6

Constraints:
  - 1 <= n <= 10^4
  - 1 <= k <= 10^5

Hint: same[i] = diff[i-1] (current same as prev). diff[i] = (k-1)*(same[i-1]+diff[i-1]).
Pattern: DP
"""


def paint_fence(n: int, k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert paint_fence(3, 2) == 6
    assert paint_fence(2, 4) == 16
    assert paint_fence(1, 3) == 3
    print("All tests passed!")
