"""
Problem: Combination Sum (LC 39) | Smart-DSA Day 33 | Medium
Pattern: Backtracking
Time target: 30 minutes

Given an array of distinct positive integers candidates and a target integer,
return a list of all unique combinations of candidates that sum to target.
The same number may be chosen from candidates an unlimited number of times.
Return the combinations in any order.

Example 1:
  Input: candidates = [2, 3, 6, 7], target = 7
  Output: [[2,2,3],[7]]

Example 2:
  Input: candidates = [2, 3, 5], target = 8
  Output: [[2,2,2,2],[2,3,3],[3,5]]

Constraints:
  - 1 <= candidates.length <= 30
  - 2 <= candidates[i] <= 40
  - All elements of candidates are distinct.
  - 1 <= target <= 40

Hint (⚠ read only after time budget is blown):
  Backtrack with a `start` index. When remaining == 0, record the path. If
  remaining < 0, prune. Loop from `start` onward (not i+1!) to allow reuse of
  the same element.
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    pass


if __name__ == "__main__":
    result1 = combination_sum([2, 3, 6, 7], 7)
    assert sorted(map(sorted, result1)) == sorted(map(sorted, [[2, 2, 3], [7]]))

    result2 = combination_sum([2, 3, 5], 8)
    assert sorted(map(sorted, result2)) == sorted(map(sorted, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]))

    result3 = combination_sum([2], 1)
    assert result3 == []
    print("All tests passed!")
