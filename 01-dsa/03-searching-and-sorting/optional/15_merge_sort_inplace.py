"""
Problem: Implement Merge Sort In-Place (GFG) | Optional | Hard
Topic: Searching and Sorting

Implement merge sort that uses O(1) extra space (in-place merge).

Example 1:
  Input: arr = [5, 6, 3, 2, 8, 7, 1, 4]
  Output: [1, 2, 3, 4, 5, 6, 7, 8]

Constraints:
  - 1 <= n <= 10^5

Hint: Shell sort–style gap-based merge or block merge technique.
Pattern: In-Place Merge Sort
"""


def merge_sort_inplace(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert merge_sort_inplace([5, 6, 3, 2, 8, 7, 1, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_sort_inplace([3, 1, 2]) == [1, 2, 3]
    print("All tests passed!")
