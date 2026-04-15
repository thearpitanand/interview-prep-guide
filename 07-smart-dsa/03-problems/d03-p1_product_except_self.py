"""
Problem: Product of Array Except Self (LC 238) | Smart-DSA Day 3 | Medium
Pattern: Arrays & Hashing (Prefix products)
Time target: 25 minutes

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all elements of nums except nums[i].
Must run in O(n) time and without using division.

Example 1:
  Input: nums = [1, 2, 3, 4]
  Output: [24, 12, 8, 6]

Example 2:
  Input: nums = [-1, 1, 0, -3, 3]
  Output: [0, 0, 9, 0, 0]

Constraints:
  - 2 <= nums.length <= 10^5
  - -30 <= nums[i] <= 30
  - The product of any prefix or suffix fits in a 32-bit integer.

Hint (⚠ read only after time budget is blown):
  Build a prefix-product array (left pass) and a suffix-product array (right
  pass). answer[i] = prefix[i] * suffix[i].
"""


def product_except_self(nums: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
    print("All tests passed!")
