"""
Problem: Binary Tree Level Order Traversal (LC 102) | Smart-DSA Day 25 | Medium
Pattern: Tree BFS
Time target: 25 minutes

Given the root of a binary tree, return the level order traversal of its
node values (i.e., left to right, level by level).

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: [[3],[9,20],[15,7]]

Example 2:
  Input: root = [1]
  Output: [[1]]

Example 3:
  Input: root = []
  Output: []

Constraints:
  - The number of nodes is in [0, 2000].
  - -1000 <= Node.val <= 1000

Hint (⚠ read only after time budget is blown):
  Use a deque. Before processing each level, snapshot len(queue) so you know
  how many nodes belong to this level. Enqueue children as you dequeue parents.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    pass


if __name__ == "__main__":
    # [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root1) == [[3], [9, 20], [15, 7]]

    # Single node
    assert level_order(TreeNode(1)) == [[1]]

    # Empty
    assert level_order(None) == []

    # [1,2,3,4,5] -> [[1],[2,3],[4,5]]
    root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert level_order(root2) == [[1], [2, 3], [4, 5]]

    print("All tests passed!")
