"""
Problem: Largest BST in Binary Tree (GFG) | Day 27 | Hard
Topic: BST

Given a binary tree, find the size of the largest subtree which is a BST.

Example 1:
  Input:     50
           /    \\
         30      60
        / \\    / \\
       5  20  45  70
                 / \\
                65  80
  Output: 5 (the subtree rooted at 60)

Constraints:
  - 1 <= n <= 10^5

Hint: Post-order: each node returns (is_bst, size, min, max). Combine bottom-up.
Pattern: Post-order DFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largest_bst(root: TreeNode) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(50,
        TreeNode(30, TreeNode(5), TreeNode(20)),
        TreeNode(60, TreeNode(45), TreeNode(70, TreeNode(65), TreeNode(80)))
    )
    assert largest_bst(root) == 5
    # Single node is always BST
    assert largest_bst(TreeNode(1)) == 1
    print("All tests passed!")
