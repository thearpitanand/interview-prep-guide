"""
Problem: Merge 2 Sorted Arrays Without Extra Space (GFG) | Day 5 | Medium
Topic: Arrays

Given two sorted arrays arr1[] and arr2[], merge them in-place so that
arr1 contains the first m smallest elements and arr2 contains the rest,
both in sorted order. No extra space allowed.

Example 1:
  Input: arr1 = [1, 5, 9, 10, 15], arr2 = [2, 3, 8, 12]
  Output: arr1 = [1, 2, 3, 5, 8], arr2 = [9, 10, 12, 15]

Constraints:
  - 1 <= m, n <= 10^5
  - 1 <= arr[i] <= 10^7

Hint: Gap method (Shell sort idea) — start with gap = ceil((m+n)/2), compare and swap.
Pattern: Gap Method / Two Pointers
"""


def merge_without_space(arr1: list[int], arr2: list[int]) -> None:
    # Write your solution here (modify in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    a1, a2 = [1, 5, 9, 10, 15], [2, 3, 8, 12]
    merge_without_space(a1, a2)
    assert a1 == [1, 2, 3, 5, 8]
    assert a2 == [9, 10, 12, 15]
    print("All tests passed!")
