"""
Problem: Check if Preorder of BST is Valid (GFG) | Optional | Medium
Topic: BST

Given an array, check if it can represent the preorder traversal of a BST.

Example 1:
  Input: pre = [2, 4, 3]
  Output: True

Example 2:
  Input: pre = [2, 4, 1]
  Output: False

Constraints:
  - 1 <= n <= 10^5

Hint: Use stack with lower bound. Maintain a min value that increases as you go right.
Pattern: Monotonic Stack
"""


def is_valid_preorder(pre: list[int]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_valid_preorder([2, 4, 3]) == True
    assert is_valid_preorder([2, 4, 1]) == False
    assert is_valid_preorder([40, 30, 35, 80, 100]) == True
    print("All tests passed!")
