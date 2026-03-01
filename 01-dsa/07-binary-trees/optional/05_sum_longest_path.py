"""
Problem: Sum of Longest Root-to-Leaf Path (GFG) | Optional | Medium
Topic: Binary Trees

Find the sum of nodes on the longest path from root to leaf.
If multiple paths have the same length, return the one with maximum sum.

Example 1:
  Input:     4
           /   \\
          2     5
         / \\   / \\
        7   1 2   3
           /
          6
  Output: 13 (path 4->2->1->6)

Constraints:
  - 1 <= n <= 10^4

Hint: DFS tracking (depth, sum). Update answer when depth increases or sum increases at same depth.
Pattern: DFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_longest_path(root: TreeNode) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(7), TreeNode(1, TreeNode(6))), TreeNode(5, TreeNode(2), TreeNode(3)))
    assert sum_longest_path(root) == 13
    print("All tests passed!")
