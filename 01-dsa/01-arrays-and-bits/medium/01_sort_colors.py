"""
Problem: Sort Colors (LC 75) | Day 4 | Medium
Topic: Arrays

Sort an array with values 0, 1, 2 in-place (Dutch National Flag).

Example:
  Input: nums = [2,0,2,1,1,0]
  Output: [0,0,1,1,2,2]

Constraints:
  - n == nums.length, 1 <= n <= 300
  - nums[i] is 0, 1, or 2

Hint: Use three pointers: low, mid, high.
Pattern: Dutch National Flag / Three Pointers
"""


def sort_colors(nums: list[int]) -> None:
    # Write your solution here (modify in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    n1 = [2, 0, 2, 1, 1, 0]
    sort_colors(n1)
    assert n1 == [0, 0, 1, 1, 2, 2]

    n2 = [2, 0, 1]
    sort_colors(n2)
    assert n2 == [0, 1, 2]
    print("All tests passed!")
