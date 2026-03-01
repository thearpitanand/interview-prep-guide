"""
Problem: Boundary Traversal (LC 545 / GFG) | Day 24 | Medium
Topic: Binary Trees

Given a binary tree, return boundary traversal in anti-clockwise order:
left boundary (top-down) + leaf nodes (left-right) + right boundary (bottom-up).

Example 1:
  Input:       1
             /   \\
            2     3
           / \\   / \\
          4   5 6   7
  Output: [1, 2, 4, 5, 6, 7, 3]

Constraints:
  - 1 <= n <= 10^5

Hint: Three parts: left boundary (exclude leaves), leaf nodes, right boundary reversed (exclude leaves).
Pattern: Tree Traversal
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boundary_traversal(root: TreeNode) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    result = boundary_traversal(root)
    assert result == [1, 2, 4, 5, 6, 7, 3]
    assert boundary_traversal(TreeNode(1)) == [1]
    print("All tests passed!")
