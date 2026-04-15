"""
Problem: Merge Intervals (LC 56) | Smart-DSA Day 48 | Medium
Pattern: Intervals — sort and sweep
Time target: 25 minutes

Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals and return an array of the non-overlapping intervals that
cover all the intervals in the input.

Example 1:
  Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
  Output: [[1,6],[8,10],[15,18]]

Example 2:
  Input: intervals = [[1,4],[4,5]]
  Output: [[1,5]]  (intervals that touch at a point are considered overlapping)

Constraints:
  - 1 <= intervals.length <= 10^4
  - intervals[i].length == 2
  - 0 <= start_i <= end_i <= 10^4

Hint (⚠ read only after time budget is blown):
  Sort by start time. Keep a merged list. For each interval:
  if merged is empty OR current start > last merged end → append.
  Else extend last merged end: merged[-1][1] = max(merged[-1][1], current end).
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    pass


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert merge([[1, 1]]) == [[1, 1]]
    print("All tests passed!")
