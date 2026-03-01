"""
Problem: Kth Largest Element in BST (GFG) | Optional | Easy
Topic: BST

Find the kth largest element in a BST.

Example 1:
  Input: BST = [4,2,9], k = 2
  Output: 4  # sorted: [2,4,9], 2nd largest = 4

Constraints:
  - 1 <= k <= n

Hint: Reverse inorder (right, root, left) and count.
Pattern: Reverse Inorder
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_largest_bst(root: TreeNode, k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2), TreeNode(9))
    assert kth_largest_bst(root, 1) == 9
    assert kth_largest_bst(root, 2) == 4
    print("All tests passed!")
