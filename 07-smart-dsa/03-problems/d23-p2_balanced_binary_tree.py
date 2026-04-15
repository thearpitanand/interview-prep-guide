"""
Problem: Balanced Binary Tree (LC 110) | Smart-DSA Day 23 | Medium
Pattern: Tree DFS
Time target: 20 minutes

Given the root of a binary tree, determine if it is height-balanced. A tree
is height-balanced if for every node the heights of its left and right subtrees
differ by at most one.

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: True

Example 2:
  Input: root = [1,2,2,3,3,null,null,4,4]
  Output: False

Example 3:
  Input: root = []
  Output: True

Constraints:
  - The number of nodes is in [0, 5000].
  - -10^4 <= Node.val <= 10^4

Hint (⚠ read only after time budget is blown):
  Have the helper return -1 as a sentinel for "unbalanced". If either child
  returns -1, or abs(left - right) > 1, return -1. Otherwise return
  1 + max(left, right). Call is_balanced(root) by checking helper != -1.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    pass


if __name__ == "__main__":
    # [3,9,20,null,null,15,7] -> True
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(root1) is True

    # [1,2,2,3,3,null,null,4,4] -> False
    root2 = TreeNode(1,
                     TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
                     TreeNode(2))
    assert is_balanced(root2) is False

    # Empty -> True
    assert is_balanced(None) is True

    # Single node -> True
    assert is_balanced(TreeNode(1)) is True

    print("All tests passed!")
