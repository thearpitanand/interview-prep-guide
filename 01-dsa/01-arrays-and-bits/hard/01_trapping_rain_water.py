"""
Problem: Trapping Rain Water (LC 42) | Day 6 | Hard
Topic: Arrays

Given n non-negative integers representing an elevation map,
compute how much water it can trap after raining.

Example:
  Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6

Constraints:
  - n == height.length, 1 <= n <= 2 * 10^4

Hint: Water at each position = min(max_left, max_right) - height.
      Two-pointer approach is O(1) space.
Pattern: Two Pointers
"""


def trap(height: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([]) == 0
    print("All tests passed!")
