"""
Problem: Subsets (LC 78) | Day 7 | Medium
Topic: Bit Manipulation

Given an integer array of unique elements, return all subsets.

Example:
  Input: nums = [1,2,3]
  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Hint: Use bitmask: for n elements, iterate 0 to 2^n - 1.
Pattern: Bitmask / Backtracking
"""


def subsets(nums: list[int]) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = subsets([1, 2, 3])
    assert len(result) == 8
    assert [] in result
    assert [1, 2, 3] in result
    print("All tests passed!")
