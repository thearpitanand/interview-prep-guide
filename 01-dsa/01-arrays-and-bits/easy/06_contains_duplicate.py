"""
Problem: Contains Duplicate (LC 217) | Day 5 | Easy
Topic: Arrays

Return true if any value appears at least twice.

Example 1:
  Input: nums = [1,2,3,1]
  Output: True

Example 2:
  Input: nums = [1,2,3,4]
  Output: False

Constraints:
  - 1 <= nums.length <= 10^5

Hint: Use a set.
Pattern: Hash Set
"""


def contains_duplicate(nums: list[int]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    print("All tests passed!")
