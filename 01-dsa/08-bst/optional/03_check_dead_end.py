"""
Problem: Check for Dead End in BST (GFG) | Optional | Easy
Topic: BST

Given a BST with positive integers, check if it has a dead end (a leaf node
where you can't insert any element).

Example 1:
  Input: BST = [8,5,9,2,7,null,null,1]
  Output: True (at node 1: can't insert 0, and 2 already exists)

Constraints:
  - All values are positive (>= 1)

Hint: Pass range [min, max] down. If leaf and min == max, it's a dead end.
Pattern: DFS with Range
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_dead_end(root: TreeNode) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(8, TreeNode(5, TreeNode(2, TreeNode(1)), TreeNode(7)), TreeNode(9))
    assert has_dead_end(root) == True
    assert has_dead_end(TreeNode(8, TreeNode(3), TreeNode(10))) == False
    print("All tests passed!")
