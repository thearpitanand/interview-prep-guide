"""
Problem: Kth Ancestor of a Node (GFG) | Optional | Hard
Topic: Binary Trees

Given a binary tree, a node, and k, find the kth ancestor of that node.

Example 1:
  Input: root = [1,2,3,4,5], node = 5, k = 2
  Output: 1

Constraints:
  - 1 <= n <= 10^5
  - 1 <= k <= depth of node

Hint: Find path from root to node, return path[-k-1].
Pattern: DFS + Path Tracking
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_ancestor(root: TreeNode, node: int, k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert kth_ancestor(root, 5, 2) == 1
    assert kth_ancestor(root, 5, 1) == 2
    print("All tests passed!")
