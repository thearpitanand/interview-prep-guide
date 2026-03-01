"""
Problem: Replace with Least Greater on Right (GFG) | Optional | Medium
Topic: BST

Given an array, replace every element with the least greater element on its
right. If none exists, replace with -1.

Example 1:
  Input: arr = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
  Output: [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1]

Constraints:
  - 1 <= n <= 10^5

Hint: Process from right, insert into BST. For each element, find inorder successor.
Pattern: BST / Sorted Set
"""


def replace_least_greater(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = replace_least_greater([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28])
    assert result[-1] == -1
    assert result[-2] == -1
    print("All tests passed!")
