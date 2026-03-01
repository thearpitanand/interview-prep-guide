"""
Problem: Single Number (LC 136) | Day 7 | Easy
Topic: Bit Manipulation

Every element appears twice except one. Find it.

Example 1:
  Input: nums = [2,2,1]
  Output: 1

Example 2:
  Input: nums = [4,1,2,1,2]
  Output: 4

Constraints:
  - 1 <= nums.length <= 3 * 10^4

Hint: XOR all elements. a ^ a = 0, a ^ 0 = a.
Pattern: XOR
"""


def single_number(nums: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    print("All tests passed!")
