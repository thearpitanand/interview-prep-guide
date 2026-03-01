"""
Problem: Count Derangements (GFG) | Optional | Medium
Topic: Dynamic Programming

Count permutations where no element appears in its original position.

Example 1:
  Input: n = 3
  Output: 2  # [2,3,1] and [3,1,2]

Constraints:
  - 1 <= n <= 10^4

Hint: D(n) = (n-1) * (D(n-1) + D(n-2)).
Pattern: DP
"""


def count_derangements(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_derangements(3) == 2
    assert count_derangements(4) == 9
    assert count_derangements(1) == 0
    print("All tests passed!")
