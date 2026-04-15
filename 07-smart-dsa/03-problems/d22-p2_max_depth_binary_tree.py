"""
Problem: Maximum Depth of Binary Tree (LC 104) | Smart-DSA Day 22 | Easy
Pattern: Tree DFS
Time target: 15 minutes

Given the root of a binary tree, return its maximum depth — the number of
nodes along the longest path from the root node down to the farthest leaf.

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: 3

Example 2:
  Input: root = [1,null,2]
  Output: 2

Constraints:
  - The number of nodes is in [0, 10^4].
  - -100 <= Node.val <= 100

Hint (⚠ read only after time budget is blown):
  max_depth(root) = 0 if root is None else 1 + max(max_depth(left), max_depth(right)).
  One line once you see the pattern.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    pass


if __name__ == "__main__":
    # [3,9,20,null,null,15,7] -> depth 3
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root1) == 3

    # [1,null,2] -> depth 2
    root2 = TreeNode(1, None, TreeNode(2))
    assert max_depth(root2) == 2

    # Single node
    assert max_depth(TreeNode(1)) == 1

    # Empty
    assert max_depth(None) == 0

    print("All tests passed!")
