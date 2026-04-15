"""
Problem: Diameter of Binary Tree (LC 543) | Smart-DSA Day 23 | Medium
Pattern: Tree DFS
Time target: 25 minutes

Given the root of a binary tree, return the length of the diameter. The
diameter is the length of the longest path between any two nodes (measured
in edges). The path may or may not pass through the root.

Example 1:
  Input: root = [1,2,3,4,5]
  Output: 3
  Explanation: Path [4,2,1,3] or [5,2,1,3] has length 3.

Example 2:
  Input: root = [1,2]
  Output: 1

Constraints:
  - The number of nodes is in [1, 10^4].
  - -100 <= Node.val <= 100

Hint (⚠ read only after time budget is blown):
  The helper returns the depth of the subtree. At each node update a global
  max with left_depth + right_depth. The diameter at a node is the sum of the
  longest left and right paths through it.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    pass


if __name__ == "__main__":
    # [1,2,3,4,5] -> 3
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(root1) == 3

    # [1,2] -> 1
    root2 = TreeNode(1, TreeNode(2))
    assert diameter_of_binary_tree(root2) == 1

    # Single node -> 0
    assert diameter_of_binary_tree(TreeNode(1)) == 0

    # Linear chain [1,2,3,4] -> 3
    root3 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert diameter_of_binary_tree(root3) == 3

    print("All tests passed!")
