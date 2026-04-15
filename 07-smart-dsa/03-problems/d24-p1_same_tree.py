"""
Problem: Same Tree (LC 100) | Smart-DSA Day 24 | Easy
Pattern: Tree DFS
Time target: 15 minutes

Given the roots of two binary trees p and q, write a function to check if
they are the same. Two trees are the same if they are structurally identical
and the nodes have the same values.

Example 1:
  Input: p = [1,2,3], q = [1,2,3]
  Output: True

Example 2:
  Input: p = [1,2], q = [1,null,2]
  Output: False

Example 3:
  Input: p = [1,2,1], q = [1,1,2]
  Output: False

Constraints:
  - The number of nodes in both trees is in [0, 100].
  - -10^4 <= Node.val <= 10^4

Hint (⚠ read only after time budget is blown):
  Base cases: both None → True; one None → False; values differ → False.
  Recurse on both subtrees and AND the results.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    pass


if __name__ == "__main__":
    # [1,2,3] vs [1,2,3] -> True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p1, q1) is True

    # [1,2] vs [1,null,2] -> False
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p2, q2) is False

    # [1,2,1] vs [1,1,2] -> False
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(p3, q3) is False

    # Both empty -> True
    assert is_same_tree(None, None) is True

    print("All tests passed!")
