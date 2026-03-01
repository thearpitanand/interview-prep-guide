"""
Problem: Reverse Level Order Traversal (GFG) | Optional | Easy
Topic: Binary Trees

Given a binary tree, return the reverse level order traversal
(bottom to top, left to right at each level).

Example 1:
  Input:     1
           /   \\
          2     3
         / \\
        4   5
  Output: [4, 5, 2, 3, 1]

Constraints:
  - 0 <= n <= 10^5

Hint: BFS with queue, reverse the result. Or use stack.
Pattern: BFS + Reverse
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverse_level_order(root: TreeNode) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert reverse_level_order(root) == [4, 5, 2, 3, 1]
    assert reverse_level_order(None) == []
    print("All tests passed!")
