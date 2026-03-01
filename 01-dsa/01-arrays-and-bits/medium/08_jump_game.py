"""
Problem: Jump Game II (LC 45) | Day 8 | Medium
Topic: Arrays

Return minimum number of jumps to reach the last index.

Example:
  Input: nums = [2,3,1,1,4]
  Output: 2

Constraints:
  - 1 <= nums.length <= 10^4

Hint: BFS-like greedy approach. Track the farthest you can reach.
Pattern: Greedy
"""


def jump(nums: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
    assert jump([1]) == 0
    print("All tests passed!")
