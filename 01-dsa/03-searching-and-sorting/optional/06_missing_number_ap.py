"""
Problem: Missing Number in AP (GFG) | Optional | Easy
Topic: Searching and Sorting

Given a sorted array representing an arithmetic progression with one element
missing, find the missing number.

Example 1:
  Input: arr = [2, 4, 8, 10, 12, 14]
  Output: 6

Constraints:
  - n >= 3
  - Exactly one element missing

Hint: Binary search — check if arr[mid] matches expected value at that index.
Pattern: Binary Search
"""


def missing_in_ap(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert missing_in_ap([2, 4, 8, 10, 12, 14]) == 6
    assert missing_in_ap([1, 6, 11, 16, 21, 31]) == 26
    print("All tests passed!")
