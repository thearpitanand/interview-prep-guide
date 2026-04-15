"""
Problem: Permutations (LC 46) | Smart-DSA Day 32 | Medium
Pattern: Backtracking
Time target: 25 minutes

Given an array nums of distinct integers, return all possible permutations
in any order.

Example 1:
  Input: nums = [1, 2, 3]
  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
  Input: nums = [0, 1]
  Output: [[0,1],[1,0]]

Example 3:
  Input: nums = [1]
  Output: [[1]]

Constraints:
  - 1 <= nums.length <= 6
  - -10 <= nums[i] <= 10
  - All integers in nums are unique.

Hint (⚠ read only after time budget is blown):
  Use a `used` boolean array. At each step, try every unused element. Add it
  to the path, mark used, recurse. When the path length equals nums length,
  record the permutation. Backtrack by popping and marking unused.
"""


def permute(nums: list[int]) -> list[list[int]]:
    pass


if __name__ == "__main__":
    result1 = permute([1, 2, 3])
    expected1 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert sorted(result1) == sorted(expected1)

    result2 = permute([0, 1])
    assert sorted(result2) == sorted([[0, 1], [1, 0]])

    result3 = permute([1])
    assert result3 == [[1]]
    print("All tests passed!")
