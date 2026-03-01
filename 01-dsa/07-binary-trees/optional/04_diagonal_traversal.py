"""
Problem: Diagonal Traversal (GFG) | Optional | Medium
Topic: Binary Trees

Print all diagonal elements of a binary tree.

Example 1:
  Input:     8
           /   \\
          3    10
         / \\     \\
        1   6    14
           / \\   /
          4   7 13
  Output: [[8,10,14], [3,6,7,13], [1,4]]

Constraints:
  - 1 <= n <= 10^5

Hint: BFS with diagonal distance (going right stays same diagonal, going left increments).
Pattern: BFS + Diagonal Distance
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diagonal_traversal(root: TreeNode) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
    result = diagonal_traversal(root)
    assert result[0] == [8, 10, 14]
    print("All tests passed!")
