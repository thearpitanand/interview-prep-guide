"""
Problem: Majority Element - Moore's Voting (LC 169) | Day 12 | Easy
Topic: Searching and Sorting

Given an array of size n, find the element that appears more than n/2 times
(majority element). It is guaranteed that the majority element always exists.

Example 1:
  Input: nums = [3, 2, 3]
  Output: 3

Example 2:
  Input: nums = [2, 2, 1, 1, 1, 2, 2]
  Output: 2

Constraints:
  - n == nums.length
  - 1 <= n <= 5 * 10^4
  - -10^9 <= nums[i] <= 10^9

Hint: Boyer-Moore Voting — maintain a candidate and count. When count drops to 0, pick new candidate.
Pattern: Boyer-Moore Voting Algorithm
"""


def majority_element(nums: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element([1]) == 1
    print("All tests passed!")
