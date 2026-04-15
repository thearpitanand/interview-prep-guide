"""
Problem: Partition Equal Subset Sum (LC 416) | Smart-DSA Day 43 | Medium
Pattern: Dynamic Programming — 0/1 Knapsack
Time target: 30 minutes

Given an integer array nums, return True if you can partition it into two
subsets such that the sum of elements in both subsets is equal, False otherwise.
Each element must go to exactly one subset (0/1, not unbounded).

Example 1:
  Input: nums = [1, 5, 11, 5]
  Output: True  (subsets [1, 5, 5] and [11])

Example 2:
  Input: nums = [1, 2, 3, 5]
  Output: False

Constraints:
  - 1 <= nums.length <= 200
  - 1 <= nums[i] <= 100

Hint (⚠ read only after time budget is blown):
  If total sum is odd, immediately return False. Otherwise target = total // 2.
  Use a boolean dp set (or array): dp[j] = can we reach sum j using a subset?
  Start with dp = {0}. For each num, update dp by adding num to each existing
  reachable sum (iterate in reverse if using an array to avoid reuse). Return
  target in dp.
"""


def can_partition(nums: list[int]) -> bool:
    pass


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1, 1]) is True
    assert can_partition([1, 2, 5]) is False
    assert can_partition([3, 3, 3, 4, 5]) is True   # [3,3,3] = 9, [4,5] = 9
    print("All tests passed!")
