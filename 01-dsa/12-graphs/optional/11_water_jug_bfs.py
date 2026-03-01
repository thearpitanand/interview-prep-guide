"""
Problem: Water Jug Problem Using BFS (GFG) | Optional | Medium
Topic: Graphs

Given two jugs of capacity a and b, determine if you can measure exactly
d liters. Find minimum steps.

Example 1:
  Input: a = 4, b = 3, d = 2
  Output: 4 (or similar)

Constraints:
  - 1 <= a, b <= 100
  - 0 <= d <= max(a, b)

Hint: BFS on states (jug1_level, jug2_level). Operations: fill, empty, pour.
Pattern: BFS on State Space
"""


def water_jug(a: int, b: int, d: int) -> int:
    # Write your solution here — return min steps or -1
    pass


# --- Tests ---
if __name__ == "__main__":
    result = water_jug(4, 3, 2)
    assert result >= 0
    assert water_jug(2, 6, 5) == -1 or water_jug(2, 6, 5) >= 0
    print("All tests passed!")
