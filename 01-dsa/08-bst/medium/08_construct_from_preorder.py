"""
Problem: Construct BST from Preorder (LC 1008) | Day 27 | Medium
Topic: BST

Given an array of values representing the preorder traversal of a BST,
construct the tree.

Example 1:
  Input: preorder = [8, 5, 1, 7, 10, 12]
  Output: BST with root 8

Constraints:
  - 1 <= preorder.length <= 100
  - 1 <= preorder[i] <= 10^8
  - All values are unique

Hint: Use upper bound approach: recursively build with max constraint. O(n).
Pattern: Recursion with Bounds
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_from_preorder(preorder: list[int]) -> TreeNode:
    # Write your solution here
    pass


def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


# --- Tests ---
if __name__ == "__main__":
    tree = bst_from_preorder([8, 5, 1, 7, 10, 12])
    assert tree.val == 8
    assert preorder_traversal(tree) == [8, 5, 1, 7, 10, 12]
    print("All tests passed!")
