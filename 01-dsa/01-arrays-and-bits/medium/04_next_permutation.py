"""
Problem: Next Permutation (LC 31) | Day 5 | Medium
Topic: Arrays

Find the next lexicographically greater permutation.
If not possible, rearrange to the lowest (sorted ascending).

Example 1:
  Input: nums = [1,2,3]
  Output: [1,3,2]

Example 2:
  Input: nums = [3,2,1]
  Output: [1,2,3]

Hint: Find rightmost ascending pair, swap with next larger, reverse suffix.
Pattern: Array Manipulation
"""


def next_permutation(nums: list[int]) -> None:
    # Write your solution here (modify in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    n1 = [1, 2, 3]
    next_permutation(n1)
    assert n1 == [1, 3, 2]

    n2 = [3, 2, 1]
    next_permutation(n2)
    assert n2 == [1, 2, 3]

    n3 = [1, 1, 5]
    next_permutation(n3)
    assert n3 == [1, 5, 1]
    print("All tests passed!")
