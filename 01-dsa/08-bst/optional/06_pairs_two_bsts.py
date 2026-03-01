"""
Problem: Count Pairs from 2 BSTs with Sum X (GFG) | Optional | Medium
Topic: BST

Given two BSTs and a value X, count pairs (one from each BST) with sum = X.

Example 1:
  Input: BST1 = [5,3,7,2,4,6,8], BST2 = [10,6,15,3,8,11,18], x = 16
  Output: 3 (pairs: (5,11), (6,10), (8,8))

Constraints:
  - 1 <= n1, n2 <= 10^5

Hint: Inorder of BST1 + reverse inorder of BST2, two pointer technique.
Pattern: BST Iterator / Two Pointers
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_pairs(root1: TreeNode, root2: TreeNode, x: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    bst1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
    bst2 = TreeNode(10, TreeNode(6, TreeNode(3), TreeNode(8)), TreeNode(15, TreeNode(11), TreeNode(18)))
    assert count_pairs(bst1, bst2, 16) == 3
    print("All tests passed!")
