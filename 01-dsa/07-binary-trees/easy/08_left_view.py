"""
Problem: Left View of Tree (GFG) | Day 23 | Easy
Topic: Binary Trees

Given a binary tree, return the left view (first node at each level).

Example 1:
  Input:     1
           /   \\
          2     3
         / \\
        4   5
  Output: [1, 2, 4]

Constraints:
  - 0 <= n <= 10^5

Hint: BFS level-order, take first element of each level. Or DFS tracking max level seen.
Pattern: BFS / DFS Level Tracking
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root: TreeNode) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert left_view(root) == [1, 2, 4]
    assert left_view(None) == []
    assert left_view(TreeNode(1)) == [1]
    print("All tests passed!")
