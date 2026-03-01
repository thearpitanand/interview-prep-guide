"""
Problem: Largest Subtree Sum (GFG) | Optional | Medium
Topic: Binary Trees

Find the largest sum subtree in a binary tree.

Example 1:
  Input:     1
           /   \\
         -2     3
         / \\   / \\
        4   5 -6   2
  Output: 7 (subtree rooted at -2: -2+4+5=7)

Constraints:
  - 1 <= n <= 10^5

Hint: Post-order DFS, compute subtree sums, track maximum.
Pattern: Post-order DFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largest_subtree_sum(root: TreeNode) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(-2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(-6), TreeNode(2)))
    assert largest_subtree_sum(root) == 7
    print("All tests passed!")
