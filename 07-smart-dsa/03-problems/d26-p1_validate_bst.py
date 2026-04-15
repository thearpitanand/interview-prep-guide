"""
Problem: Validate Binary Search Tree (LC 98) | Smart-DSA Day 26 | Medium
Pattern: BST
Time target: 25 minutes

Given the root of a binary tree, determine if it is a valid binary search tree.
A valid BST requires:
  - All nodes in the left subtree have values strictly less than the node's value.
  - All nodes in the right subtree have values strictly greater than the node's value.
  - Both subtrees are also valid BSTs.

Example 1:
  Input: root = [2,1,3]
  Output: True

Example 2:
  Input: root = [5,1,4,null,null,3,6]
  Output: False  (right child 4 < root 5)

Constraints:
  - The number of nodes is in [1, 10^4].
  - -2^31 <= Node.val <= 2^31 - 1

Hint (⚠ read only after time budget is blown):
  Pass (low, high) bounds down recursively. A node is valid only if
  low < node.val < high. Left subtrees get high=node.val; right subtrees get
  low=node.val. Initial bounds: (-inf, +inf).
"""

import math


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    pass


if __name__ == "__main__":
    # [2,1,3] -> True
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root1) is True

    # [5,1,4,null,null,3,6] -> False
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(root2) is False

    # Single node -> True
    assert is_valid_bst(TreeNode(1)) is True

    # Classic trap: [10,5,15,null,null,6,20] -> False (6 < 10, violates root)
    root3 = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
    assert is_valid_bst(root3) is False

    print("All tests passed!")
