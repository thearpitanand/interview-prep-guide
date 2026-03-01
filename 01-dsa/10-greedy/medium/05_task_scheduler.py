"""
Problem: Task Scheduler
Day: 30 | Difficulty: Medium | Topic: Greedy
Link: https://leetcode.com/problems/task-scheduler/

Description:
    You are given an array of CPU tasks, each represented by a letter A to Z,
    and a cooling interval n. Each cycle or interval allows the completion of
    one task. There must be at least n intervals between two same tasks.
    Return the minimum number of intervals the CPU will take to finish all
    the given tasks.

Examples:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B

    Input: tasks = ["A","A","A","B","B","B"], n = 0
    Output: 6
    Explanation: No cooldown needed, just run all tasks: 6 intervals.

    Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    Output: 16

Constraints:
    - 1 <= tasks.length <= 10^4
    - tasks[i] is an uppercase English letter
    - 0 <= n <= 100

Hint:
    The most frequent task determines the structure. If max frequency is f,
    we need (f - 1) groups of size (n + 1), plus the number of tasks that
    share the max frequency. The answer is max(len(tasks), calculated_slots).

Pattern: Greedy - the most frequent task creates (f-1) "frames" of size (n+1).
    Fill idle slots with other tasks. Answer = max(total_tasks, frame_slots).
"""

from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"tasks": ["A", "A", "A", "B", "B", "B"], "n": 2, "expected": 8},
        {"tasks": ["A", "A", "A", "B", "B", "B"], "n": 0, "expected": 6},
        {"tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], "n": 2, "expected": 16},
        {"tasks": ["A"], "n": 0, "expected": 1},
        {"tasks": ["A", "B", "C", "D"], "n": 3, "expected": 4},
        {"tasks": ["A", "A", "B", "B", "C", "C"], "n": 2, "expected": 6},
    ]

    for i, t in enumerate(tests):
        result = least_interval(t["tasks"], t["n"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
