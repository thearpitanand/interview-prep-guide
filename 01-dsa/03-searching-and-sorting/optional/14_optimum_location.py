"""
Problem: Optimum Location to Minimize Distance (GFG) | Optional | Hard
Topic: Searching and Sorting

Given N points on a line, find a point such that the sum of distances from
all given points is minimized. Points can be at fractional positions.

Example 1:
  Input: points = [1, 2, 3]
  Output: 2  # median minimizes L1 distance

Constraints:
  - 1 <= n <= 10^5

Hint: The median minimizes sum of absolute deviations for L1; for L2, use ternary search.
Pattern: Ternary Search / Math
"""


def optimum_location(points: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert optimum_location([1, 2, 3]) == 2
    assert optimum_location([4, 1]) in [1, 2, 3, 4]
    print("All tests passed!")
