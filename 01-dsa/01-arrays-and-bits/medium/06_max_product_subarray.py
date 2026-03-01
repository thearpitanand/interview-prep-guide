"""
Problem: Maximum Product Subarray (LC 152) | Day 5 | Medium
Topic: Arrays

Find the contiguous subarray with the largest product.

Example:
  Input: nums = [2,3,-2,4]
  Output: 6 (subarray [2,3])

Constraints:
  - 1 <= nums.length <= 2 * 10^4

Hint: Track both max and min product (negative * negative = positive).
Pattern: Kadane's Variant
"""


def max_product(nums: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-2, 3, -4]) == 24
    print("All tests passed!")
