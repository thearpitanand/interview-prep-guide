"""
Problem: Car Fleet (LC 853) | Smart-DSA Day 17 | Medium
Pattern: Monotonic Stack
Time target: 25 minutes

There are n cars at given positions on a one-lane road heading to the same
target miles away. A car can never pass another car, but it can catch up.
If a faster car catches a slower one, they form a fleet and arrive together.

Given arrays position and speed (same length), return the number of car
fleets that will arrive at the target.

Example 1:
  Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
  Output: 3

Example 2:
  Input: target = 10, position = [3], speed = [3]
  Output: 1

Example 3:
  Input: target = 100, position = [0,2,4], speed = [4,2,1]
  Output: 1

Constraints:
  - n == position.length == speed.length
  - 1 <= n <= 10^5
  - 0 < target <= 10^6
  - 0 <= position[i] < target
  - 0 < speed[i] <= 10^6
  - All positions are unique.

Hint (⚠ read only after time budget is blown):
  Sort cars by position descending. Compute time = (target - pos) / speed for
  each. Use a stack: if current car's time > stack top time, it forms a new
  fleet (push); otherwise it catches up and joins the fleet ahead.
"""


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert car_fleet(10, [3], [3]) == 1
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1
    assert car_fleet(10, [6, 8], [3, 2]) == 2
    print("All tests passed!")
