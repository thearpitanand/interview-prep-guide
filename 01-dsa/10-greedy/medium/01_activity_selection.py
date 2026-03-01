"""
Problem: Non-overlapping Intervals (Activity Selection variant)
Day: 29 | Difficulty: Medium | Topic: Interval Greedy
Link: https://leetcode.com/problems/non-overlapping-intervals/

Description:
    Given an array of intervals where intervals[i] = [start_i, end_i],
    return the minimum number of intervals you need to remove to make the
    rest of the intervals non-overlapping.
    Note: Intervals that only touch at a point are non-overlapping.
    For example, [1, 2] and [2, 3] are non-overlapping.

Examples:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: Remove [1,3] and the rest are non-overlapping.

    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2

    Input: intervals = [[1,2],[2,3]]
    Output: 0

Constraints:
    - 1 <= intervals.length <= 10^5
    - intervals[i].length == 2
    - -5 * 10^4 <= start_i < end_i <= 5 * 10^4

Hint:
    This is the classic activity selection problem in disguise. Sort by end
    time. Count the maximum number of non-overlapping intervals. The answer
    is total intervals minus that count.

Pattern: Sort by end time, greedily pick intervals that don't overlap with
    the last selected interval. Removals = total - selected.
"""

from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"intervals": [[1, 2], [2, 3], [3, 4], [1, 3]], "expected": 1},
        {"intervals": [[1, 2], [1, 2], [1, 2]], "expected": 2},
        {"intervals": [[1, 2], [2, 3]], "expected": 0},
        {"intervals": [[1, 100], [11, 22], [1, 11], [2, 12]], "expected": 2},
        {"intervals": [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], "expected": 2},
        {"intervals": [[1, 2]], "expected": 0},
    ]

    for i, t in enumerate(tests):
        result = erase_overlap_intervals(t["intervals"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
