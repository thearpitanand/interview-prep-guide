"""
Problem: Subsets (LC 78) | Smart-DSA Day 32 | Medium
Pattern: Backtracking
Time target: 25 minutes

Given an integer array nums of unique elements, return all possible subsets
(the power set). The solution set must not contain duplicate subsets.
Return the answer in any order.

Example 1:
  Input: nums = [1, 2, 3]
  Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
  Input: nums = [0]
  Output: [[], [0]]

Constraints:
  - 1 <= nums.length <= 10
  - -10 <= nums[i] <= 10
  - All elements of nums are unique.

Hint (⚠ read only after time budget is blown):
  Backtrack from index `start`. Append a copy of the current path at every
  call (not just the base case). Loop from `start` to end: choose nums[i],
  recurse with i+1, then pop (unchoose).
"""


def subsets(nums: list[int]) -> list[list[int]]:
    pass


if __name__ == "__main__":
    result1 = subsets([1, 2, 3])
    expected1 = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(map(sorted, result1)) == sorted(map(sorted, expected1))

    result2 = subsets([0])
    assert sorted(map(tuple, result2)) == sorted(map(tuple, [[], [0]]))

    result3 = subsets([1, 2])
    expected3 = [[], [1], [2], [1, 2]]
    assert sorted(map(sorted, result3)) == sorted(map(sorted, expected3))
    print("All tests passed!")
