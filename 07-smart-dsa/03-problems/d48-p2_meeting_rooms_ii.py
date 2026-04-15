"""
Problem: Meeting Rooms II (LC 253) | Smart-DSA Day 48 | Medium
Pattern: Intervals — min-heap or sorted events
Time target: 25 minutes

Given an array of meeting time intervals intervals[i] = [start_i, end_i],
return the minimum number of conference rooms required so all meetings can
proceed without conflict.

Example 1:
  Input: intervals = [[0,30],[5,10],[15,20]]
  Output: 2

Example 2:
  Input: intervals = [[7,10],[2,4]]
  Output: 1

Constraints:
  - 1 <= intervals.length <= 10^4
  - 0 <= start_i < end_i <= 10^6

Hint (⚠ read only after time budget is blown):
  Sort by start. Use a min-heap of end times. For each meeting:
  if heap[0] <= start, a room is free — pop it (meeting ended).
  Push current end onto heap. Answer is heap size at the end.
  Alternatively: separate sorted starts and ends arrays, two-pointer sweep.
"""


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    pass


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([[1, 5], [2, 6], [3, 7]]) == 3
    assert min_meeting_rooms([[1, 10]]) == 1
    assert min_meeting_rooms([[1, 4], [5, 9]]) == 1
    print("All tests passed!")
