"""
Problem: House Robber III / Max Sum No Adjacent (LC 337) | Optional | Medium
Topic: Binary Trees

A thief robs houses arranged in a binary tree. Adjacent houses (parent-child)
can't both be robbed. Find max amount.

Example 1:
  Input:     3
           /   \\
          2     3
           \\     \\
            3     1
  Output: 7 (3 + 3 + 1)

Constraints:
  - 1 <= n <= 10^4

Hint: DFS returns (rob_this, skip_this) for each node.
Pattern: Tree DP
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: TreeNode) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    assert rob(root) == 7
    assert rob(TreeNode(1)) == 1
    print("All tests passed!")
