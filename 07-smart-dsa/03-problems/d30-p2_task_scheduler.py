"""
Problem: Task Scheduler (LC 621) | Smart-DSA Day 30 | Medium
Pattern: Heap + Greedy
Time target: 30 minutes

Given a list of CPU tasks (characters A-Z) and a cooldown integer n, return
the minimum number of intervals needed to finish all tasks. The CPU must wait
at least n intervals before running the same task type again. Idle counts as
an interval.

Example 1:
  Input: tasks = ["A","A","A","B","B","B"], n = 2
  Output: 8
  Explanation: A -> B -> idle -> A -> B -> idle -> A -> B

Example 2:
  Input: tasks = ["A","A","A","B","B","B"], n = 0
  Output: 6

Example 3:
  Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
  Output: 16

Constraints:
  - 1 <= tasks.length <= 10^4
  - tasks[i] is uppercase English letter.
  - 0 <= n <= 100

Hint (⚠ read only after time budget is blown):
  Use a max-heap of frequencies and a cooldown queue of (freq, available_at)
  tuples. Each tick: pop the most frequent ready task (decrement freq), push it
  to the cooldown queue for time + n + 1. When nothing is ready, idle.
"""
import heapq
from collections import Counter, deque


def least_interval(tasks: list[str], n: int) -> int:
    pass


if __name__ == "__main__":
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
    assert least_interval(["A"], 0) == 1
    print("All tests passed!")
