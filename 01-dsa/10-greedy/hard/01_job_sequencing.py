"""
Problem: Job Sequencing with Deadlines
Day: 30 | Difficulty: Hard | Topic: Greedy
Link: GeeksforGeeks Classic

Description:
    Given a set of n jobs where each job i has a deadline and a profit
    associated with it. Each job takes 1 unit of time to complete and only
    one job can be scheduled at a time. We earn the profit if and only if
    the job is completed by its deadline. Find the number of jobs done and
    the maximum profit.
    Jobs are given as tuples: (job_id, deadline, profit).

Examples:
    Input: jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
    Output: (2, 60)
    Explanation: Job 3 (profit 40) at time slot 1, Job 1 (profit 20) at
                 time slot 4. Total = 60, 2 jobs done.

    Input: jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)]
    Output: (2, 127)
    Explanation: Job 1 (profit 100) at slot 2, Job 3 (profit 27) at slot 1.

Constraints:
    - 1 <= n <= 10^5
    - 1 <= deadline <= n
    - 1 <= profit <= 500

Hint:
    Sort jobs by profit in descending order. For each job, find the latest
    available time slot at or before its deadline and assign it there. Use
    an array to track which slots are filled.

Pattern: Greedy - sort by profit descending. For each job, try to schedule it
    at the latest possible slot before its deadline using a slot array.
"""

from typing import List, Tuple


def job_sequencing(jobs: List[Tuple[int, int, int]]) -> Tuple[int, int]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {
            "jobs": [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)],
            "expected": (2, 60),
        },
        {
            "jobs": [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)],
            "expected": (2, 127),
        },
        {
            "jobs": [(1, 1, 50)],
            "expected": (1, 50),
        },
        {
            "jobs": [(1, 2, 20), (2, 2, 30), (3, 1, 10)],
            "expected": (2, 50),
        },
        {
            "jobs": [(1, 3, 35), (2, 3, 30), (3, 3, 25), (4, 1, 20)],
            "expected": (3, 90),
        },
    ]

    for i, t in enumerate(tests):
        result = job_sequencing(t["jobs"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
