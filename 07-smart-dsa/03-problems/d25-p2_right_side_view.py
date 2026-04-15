"""
Problem: Binary Tree Right Side View (LC 199) | Smart-DSA Day 25 | Medium
Pattern: Tree BFS
Time target: 25 minutes

Given the root of a binary tree, imagine standing on the right side. Return
the values of the nodes you can see, ordered from top to bottom.

Example 1:
  Input: root = [1,2,3,null,5,null,4]
  Output: [1,3,4]

Example 2:
  Input: root = [1,null,3]
  Output: [1,3]

Example 3:
  Input: root = []
  Output: []

Constraints:
  - The number of nodes is in [0, 100].
  - -100 <= Node.val <= 100

Hint (⚠ read only after time budget is blown):
  Level-order BFS; at each level, the rightmost node is the last one processed.
  Append level[-1] (or the last node dequeued per level) to the result.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode | None) -> list[int]:
    pass


if __name__ == "__main__":
    # [1,2,3,null,5,null,4] -> [1,3,4]
    root1 = TreeNode(1,
                     TreeNode(2, None, TreeNode(5)),
                     TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root1) == [1, 3, 4]

    # [1,null,3] -> [1,3]
    root2 = TreeNode(1, None, TreeNode(3))
    assert right_side_view(root2) == [1, 3]

    # Empty
    assert right_side_view(None) == []

    # [1,2,3,4] -> [1,3,4]
    root3 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert right_side_view(root3) == [1, 3, 4]

    print("All tests passed!")
