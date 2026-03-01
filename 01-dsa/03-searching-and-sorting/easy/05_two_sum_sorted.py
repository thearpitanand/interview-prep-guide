"""
Problem: Two Sum II - Input Array Is Sorted (LC 167) | Day 12 | Easy
Topic: Searching and Sorting

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number.

Return the indices of the two numbers (1-indexed) as an integer array [index1, index2].

You may not use the same element twice. There is exactly one solution.

Example 1:
  Input: numbers = [2,7,11,15], target = 9
  Output: [1,2]
  Explanation: 2 + 7 = 9. So index1 = 1, index2 = 2.

Example 2:
  Input: numbers = [2,3,4], target = 6
  Output: [1,3]

Constraints:
  - 2 <= numbers.length <= 3 * 10^4
  - -1000 <= numbers[i] <= 1000
  - numbers is sorted in non-decreasing order
  - There is exactly one solution

Hint: Use two pointers, one at start, one at end.
      If sum < target, move left pointer right.
      If sum > target, move right pointer left.
Pattern: Two Pointers on Sorted Array
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
    assert two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    print("All tests passed!")
