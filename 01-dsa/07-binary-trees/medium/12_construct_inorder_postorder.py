"""
Problem: Construct from Inorder + Postorder (LC 106) | Day 25 | Medium
Topic: Binary Trees

Given inorder and postorder traversal of a tree, construct the binary tree.

Example 1:
  Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
  Output: tree with root 3

Constraints:
  - 1 <= n <= 3000
  - inorder.length == postorder.length
  - All values unique

Hint: Last element of postorder is root. Find it in inorder to split left/right subtrees. Recurse.
Pattern: Divide and Conquer / Recursion
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode:
    # Write your solution here
    pass


def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# --- Tests ---
if __name__ == "__main__":
    tree = build_tree([9,3,15,20,7], [9,15,7,20,3])
    assert tree.val == 3
    assert inorder_traversal(tree) == [9,3,15,20,7]
    print("All tests passed!")
