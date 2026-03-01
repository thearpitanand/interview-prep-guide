"""
Problem: Longest Consecutive Sequence (LC 128) | Day 5 | Medium
Topic: Arrays

Find the length of the longest consecutive elements sequence.
Must run in O(n) time.

Example:
  Input: nums = [100,4,200,1,3,2]
  Output: 4 (sequence [1,2,3,4])

Hint: Use a set. Only start counting from sequence starts (n-1 not in set).
Pattern: Hash Set
"""


def longest_consecutive(nums: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    print("All tests passed!")
