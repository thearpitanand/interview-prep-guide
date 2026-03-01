"""
Problem: Find the Duplicate Number (LC 287) | Day 4 | Easy
Topic: Arrays

Given an array of n+1 integers where each integer is
between 1 and n, find the duplicate number.

Example 1:
  Input: nums = [1,3,4,2,2]
  Output: 2

Example 2:
  Input: nums = [3,1,3,4,2]
  Output: 3

Constraints:
  - 1 <= n <= 10^5
  - nums.length == n + 1
  - 1 <= nums[i] <= n

Hint: Think of it as a linked list cycle problem.
Pattern: Floyd's Cycle Detection
"""


def find_duplicate(nums: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    assert find_duplicate([3, 1, 3, 4, 2]) == 3
    assert find_duplicate([1, 1]) == 1
    print("All tests passed!")
