"""
Problem: Maximum Meetings in One Room (GFG) | Optional | Easy
Topic: Greedy

Given start and end times of N meetings, find the maximum number of meetings
that can be held in one room.

Example 1:
  Input: start = [1, 3, 0, 5, 8, 5], end = [2, 4, 6, 7, 9, 9]
  Output: 4

Constraints:
  - 1 <= n <= 10^5

Hint: Sort by end time. Greedily pick meetings that start after last selected ends.
Pattern: Greedy (Activity Selection)
"""


def max_meetings(start: list[int], end: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]) == 4
    assert max_meetings([1], [2]) == 1
    print("All tests passed!")
