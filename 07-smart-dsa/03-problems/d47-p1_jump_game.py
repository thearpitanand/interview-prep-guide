"""
Problem: Jump Game (LC 55) | Smart-DSA Day 47 | Medium
Pattern: Greedy
Time target: 20 minutes

You are given an integer array nums where nums[i] represents the maximum jump
length at position i. Return True if you can reach the last index starting
from index 0, False otherwise.

Example 1:
  Input: nums = [2, 3, 1, 1, 4]
  Output: True  (jump 1 from index 0, then 3 from index 1)

Example 2:
  Input: nums = [3, 2, 1, 0, 4]
  Output: False  (always land on index 3 which has jump = 0)

Constraints:
  - 1 <= nums.length <= 10^4
  - 0 <= nums[i] <= 10^5

Hint (⚠ read only after time budget is blown):
  Track max_reach = maximum index reachable so far. Iterate i from 0 to n-1.
  If i > max_reach at any point, return False (can't reach current index).
  Otherwise update max_reach = max(max_reach, i + nums[i]).
  If loop completes without returning False, return True.
"""


def can_jump(nums: list[int]) -> bool:
    pass


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    assert can_jump([0]) is True
    assert can_jump([1, 0, 0]) is False
    assert can_jump([2, 0, 0]) is True
    print("All tests passed!")
