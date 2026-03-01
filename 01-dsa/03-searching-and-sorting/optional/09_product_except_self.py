"""
Problem: Product of Array Except Self (LC 238) | Optional | Medium
Topic: Searching and Sorting

Given an array, return an array where each element is the product of all
elements except itself. No division allowed.

Example 1:
  Input: nums = [1, 2, 3, 4]
  Output: [24, 12, 8, 6]

Constraints:
  - 2 <= n <= 10^5
  - -30 <= nums[i] <= 30

Hint: Left prefix product + right prefix product.
Pattern: Prefix/Suffix Products
"""


def product_except_self(nums: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All tests passed!")
