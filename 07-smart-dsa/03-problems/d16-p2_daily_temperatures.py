"""
Problem: Daily Temperatures (LC 739) | Smart-DSA Day 16 | Medium
Pattern: Monotonic Stack
Time target: 25 minutes

Given an array of integers temperatures representing daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after day i to get a warmer temperature. If no future day is warmer,
answer[i] == 0.

Example 1:
  Input: temperatures = [73,74,75,71,69,72,76,73]
  Output: [1,1,4,2,1,1,0,0]

Example 2:
  Input: temperatures = [30,40,50,60]
  Output: [1,1,1,0]

Example 3:
  Input: temperatures = [30,60,90]
  Output: [1,1,0]

Constraints:
  - 1 <= temperatures.length <= 10^5
  - 30 <= temperatures[i] <= 100

Hint (⚠ read only after time budget is blown):
  Maintain a stack of indices with a decreasing temperature invariant. When
  temperatures[i] > temperatures[stack top], pop and record the gap i - popped.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    assert daily_temperatures([60, 60, 60]) == [0, 0, 0]
    print("All tests passed!")
