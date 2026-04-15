"""
Problem: Course Schedule (LC 207) | Smart-DSA Day 37 | Medium
Pattern: Topological Sort / Cycle Detection
Time target: 30 minutes

There are numCourses courses (labeled 0 to numCourses-1). You are given an
array prerequisites where prerequisites[i] = [a, b] means you must take
course b before course a. Return True if you can finish all courses, otherwise
return False (a cycle exists).

Example 1:
  Input: numCourses = 2, prerequisites = [[1, 0]]
  Output: True

Example 2:
  Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
  Output: False

Constraints:
  - 1 <= numCourses <= 2000
  - 0 <= prerequisites.length <= 5000
  - prerequisites[i].length == 2
  - All pairs are unique.

Hint (⚠ read only after time budget is blown):
  Build an adjacency list and compute in-degrees. Use Kahn's algorithm: enqueue
  all nodes with in-degree 0, process them, decrement neighbors' in-degrees,
  enqueue any that hit 0. If you process all nodes, no cycle exists.
"""
from collections import deque


def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pass


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(1, []) is True
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False
    print("All tests passed!")
