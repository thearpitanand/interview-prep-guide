"""
Problem: 4Sum (LC 18) | Optional | Medium
Topic: Searching and Sorting

Given an array and a target, find all unique quadruplets [a,b,c,d] such that a+b+c+d = target.

Example 1:
  Input: nums = [1, 0, -1, 0, -2, 2], target = 0
  Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Constraints:
  - 1 <= n <= 200
  - -10^9 <= nums[i] <= 10^9

Hint: Sort, fix two elements, use two pointers for remaining two.
Pattern: Two Pointers
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = four_sum([1, 0, -1, 0, -2, 2], 0)
    expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])
    print("All tests passed!")
