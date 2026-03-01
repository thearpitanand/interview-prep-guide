"""
Problem: 3Sum (LC 15) | Day 5 | Medium
Topic: Arrays

Find all unique triplets that sum to zero.

Example:
  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]

Constraints:
  - 3 <= nums.length <= 3000

Hint: Sort, fix one element, use two pointers for the rest.
Pattern: Two Pointers
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]])

    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    print("All tests passed!")
