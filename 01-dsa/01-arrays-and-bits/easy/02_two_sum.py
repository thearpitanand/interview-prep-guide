"""
Problem: Two Sum (LC 1) | Day 4 | Easy
Topic: Arrays

Given an array of integers nums and an integer target,
return indices of the two numbers that add up to target.

Example 1:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]

Example 2:
  Input: nums = [3,2,4], target = 6
  Output: [1,2]

Constraints:
  - 2 <= nums.length <= 10^4
  - -10^9 <= nums[i] <= 10^9
  - Exactly one solution exists.

Hint: What complement do you need? Use a hash map.
Pattern: Hash Map
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All tests passed!")
