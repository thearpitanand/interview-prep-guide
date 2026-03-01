"""
Problem: Shortest Job First Scheduling (GFG) | Optional | Easy
Topic: Greedy

Given burst times of processes, find the average waiting time using SJF
(non-preemptive).

Example 1:
  Input: burst = [6, 8, 7, 3]
  Output: 7.0  # sorted: [3,6,7,8], waiting: [0,3,9,16], avg=28/4=7.0

Constraints:
  - 1 <= n <= 10^5

Hint: Sort by burst time. Calculate cumulative waiting times.
Pattern: Greedy / Sorting
"""


def sjf_avg_wait(burst: list[int]) -> float:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert sjf_avg_wait([6, 8, 7, 3]) == 7.0
    assert sjf_avg_wait([1, 2, 3]) == 1.0
    print("All tests passed!")
