"""
Problem: Convert to Sum Tree + Check Sum Tree (GFG) | Optional | Medium
Topic: Binary Trees

A Sum Tree is a tree where each node's value equals the sum of values in
its left and right subtrees. Convert a tree to a sum tree and check if a
tree is a sum tree.

Example 1:
  Input:     10
           /    \\
          -2     6
         / \\   / \\
        8  -4 7   5
  After conversion: each node = sum of original left + right subtree values

Constraints:
  - 1 <= n <= 10^4

Hint: Post-order traversal. Store old value, set node = left_sum + right_sum.
Pattern: Post-order DFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_sum_tree(root: TreeNode) -> bool:
    # Write your solution here
    pass


def convert_to_sum_tree(root: TreeNode) -> None:
    # Write your solution here (modify in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    # Check sum tree
    root = TreeNode(26, TreeNode(10, TreeNode(4), TreeNode(6)), TreeNode(3, None, TreeNode(3)))
    assert is_sum_tree(root) == True
    print("All tests passed!")
