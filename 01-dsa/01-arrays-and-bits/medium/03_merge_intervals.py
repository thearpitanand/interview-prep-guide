"""
Problem: Merge Intervals (LC 56) | Day 5 | Medium
Topic: Arrays

Merge all overlapping intervals.

Example:
  Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
  Output: [[1,6],[8,10],[15,18]]

Constraints:
  - 1 <= intervals.length <= 10^4

Hint: Sort by start time, then merge overlapping.
Pattern: Merge Intervals
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    print("All tests passed!")
