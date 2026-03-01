"""
Problem: Check if Array is Subset of Another (GFG) | Optional | Easy
Topic: Arrays

Given two arrays, check whether arr2 is a subset of arr1.

Example 1:
  Input: arr1 = [11, 1, 13, 21, 3, 7], arr2 = [11, 3, 7, 1]
  Output: True

Constraints:
  - 1 <= n, m <= 10^5

Hint: Use a hash map to count elements.
Pattern: Hashing
"""


def is_subset(arr1: list[int], arr2: list[int]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_subset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1]) == True
    assert is_subset([1, 2, 3], [1, 4]) == False
    assert is_subset([10, 5, 2, 23, 19], [19, 5, 3]) == False
    print("All tests passed!")
