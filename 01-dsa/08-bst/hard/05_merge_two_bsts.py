"""
Problem: Merge Two BSTs (GFG) | Day 27 | Hard
Topic: BST

Given two BSTs, merge them into a single balanced BST.

Example 1:
  Input: BST1 = [3, 1, 5], BST2 = [4, 2, 6]
  Output: balanced BST with elements [1, 2, 3, 4, 5, 6]

Constraints:
  - 1 <= n1, n2 <= 10^5

Hint: Inorder both BSTs to get sorted arrays, merge arrays, build balanced BST from sorted array.
Pattern: Inorder + Merge + Build Balanced BST
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_bsts(root1: TreeNode, root2: TreeNode) -> TreeNode:
    # Write your solution here
    pass


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# --- Tests ---
if __name__ == "__main__":
    bst1 = TreeNode(3, TreeNode(1), TreeNode(5))
    bst2 = TreeNode(4, TreeNode(2), TreeNode(6))
    merged = merge_bsts(bst1, bst2)
    assert sorted(inorder(merged)) == [1, 2, 3, 4, 5, 6]
    print("All tests passed!")
