"""
Problem: Top View & Bottom View (GFG) | Day 24 | Medium
Topic: Binary Trees

Given a binary tree, return the top view (first node seen at each horizontal
distance from root) and bottom view (last node at each horizontal distance).

Example 1:
  Input:     1
           /   \\
          2     3
         / \\   / \\
        4   5 6   7
  Top view: [4, 2, 1, 3, 7]
  Bottom view: [4, 6, 5 or 6, 3 or 6, 7] (depends on order)

Constraints:
  - 1 <= n <= 10^5

Hint: BFS with horizontal distance. Use ordered dict. Top view = first at each HD, Bottom = last.
Pattern: BFS + Horizontal Distance
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def top_view(root: TreeNode) -> list[int]:
    # Write your solution here
    pass


def bottom_view(root: TreeNode) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    tv = top_view(root)
    assert tv[0] == 4 and tv[-1] == 7 and 1 in tv
    bv = bottom_view(root)
    assert bv[0] == 4 and bv[-1] == 7
    print("All tests passed!")
