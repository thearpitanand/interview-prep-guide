"""
Problem: Check Leaf Nodes at Same Level (GFG) | Optional | Easy
Topic: Binary Trees

Check if all leaf nodes of a binary tree are at the same level.

Example 1:
  Input:     1
           /   \\
          2     3
  Output: True (leaves 2,3 both at level 2)

Constraints:
  - 1 <= n <= 10^5

Hint: Track first leaf level, check all others match.
Pattern: DFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaves_same_level(root: TreeNode) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert leaves_same_level(TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert leaves_same_level(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))) == False
    print("All tests passed!")
