"""
Problem: Flatten BST to Sorted List (GFG) | Optional | Easy
Topic: BST

Flatten a BST into a sorted linked list (using right pointers only).

Example 1:
  Input: BST = [5,3,7,2,4,6,8]
  Output: 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 (right pointers)

Constraints:
  - 1 <= n <= 10^5

Hint: Inorder traversal, link nodes using right pointer, set left to None.
Pattern: Inorder DFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten_bst(root: TreeNode) -> TreeNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
    head = flatten_bst(root)
    vals = []
    while head:
        assert head.left is None
        vals.append(head.val)
        head = head.right
    assert vals == [2, 3, 4, 5, 6, 7, 8]
    print("All tests passed!")
