"""
Problem: Maximum Subarray (LC 53) | Day 4 | Medium
Topic: Arrays

Find the subarray with the largest sum.

Example:
  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
  Output: 6 (subarray [4,-1,2,1])

Constraints:
  - 1 <= nums.length <= 10^5

Hint: At each position, either extend the current subarray or start new.
Pattern: Kadane's Algorithm
"""


def max_subarray(nums: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-1]) == -1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    print("All tests passed!")
