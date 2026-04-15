"""
Problem: Two Sum II — Input Array Is Sorted (LC 167) | Smart-DSA Day 4 | Easy
Pattern: Two Pointers
Time target: 15 minutes

Given a 1-indexed sorted array of integers numbers, find two numbers that add
up to target. Return their indices as [index1, index2] (1-indexed).
Exactly one solution exists; each element may be used only once.
Use only O(1) extra space.

Example 1:
  Input: numbers = [2, 7, 11, 15], target = 9
  Output: [1, 2]

Example 2:
  Input: numbers = [2, 3, 4], target = 6
  Output: [1, 3]

Constraints:
  - 2 <= numbers.length <= 3 * 10^4
  - -1000 <= numbers[i] <= 1000
  - numbers is sorted in non-decreasing order.
  - Exactly one valid answer exists.

Hint (⚠ read only after time budget is blown):
  Left pointer at 0, right pointer at end. If sum < target, move left right;
  if sum > target, move right left; if equal, return 1-indexed positions.
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    pass


if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
    print("All tests passed!")
