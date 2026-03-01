"""
Problem: Convert Binary Tree to DLL (GFG) | Optional | Hard
Topic: Binary Trees

Convert a binary tree to a doubly linked list in-place. The left pointer
should act as prev and right pointer as next. The order should be inorder.

Example 1:
  Input:     10
           /    \\
          12     15
         / \\    /
        25  30  36
  Output DLL: 25 <-> 12 <-> 30 <-> 10 <-> 36 <-> 15

Constraints:
  - 1 <= n <= 10^5

Hint: Inorder traversal, maintain a prev pointer. Link prev.right = curr, curr.left = prev.
Pattern: Inorder DFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bt_to_dll(root: TreeNode) -> TreeNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(10, TreeNode(12, TreeNode(25), TreeNode(30)), TreeNode(15, TreeNode(36)))
    head = bt_to_dll(root)
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.right
    assert vals == [25, 12, 30, 10, 36, 15]
    print("All tests passed!")
