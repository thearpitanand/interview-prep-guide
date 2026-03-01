"""
Problem: Find All Duplicate Subtrees (LC 652) | Optional | Medium
Topic: Binary Trees

Given a binary tree, return all duplicate subtrees (roots of subtrees that
appear more than once).

Example 1:
  Input:     1
           /   \\
          2     3
         /     / \\
        4     2   4
             /
            4
  Output: [[2,4], [4]]  (subtrees rooted at 2->4 and leaf 4)

Constraints:
  - 1 <= n <= 5000

Hint: Serialize each subtree, use hash map to count. Return roots with count > 1.
Pattern: Serialization + Hashing
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_duplicate_subtrees(root: TreeNode) -> list[TreeNode]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4)))
    result = find_duplicate_subtrees(root)
    vals = sorted([n.val for n in result])
    assert 4 in vals
    print("All tests passed!")
