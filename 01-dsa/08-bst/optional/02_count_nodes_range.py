"""
Problem: Count Nodes in Given Range (GFG) | Optional | Easy
Topic: BST

Count nodes in a BST that lie in a given range [low, high].

Example 1:
  Input: BST = [10,5,50,1,null,40,100], low = 5, high = 45
  Output: 3 (nodes: 5, 10, 40)

Constraints:
  - 1 <= n <= 10^5

Hint: If node < low, go right. If node > high, go left. If in range, count and go both.
Pattern: BST Traversal
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_in_range(root: TreeNode, low: int, high: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5, TreeNode(1)), TreeNode(50, TreeNode(40), TreeNode(100)))
    assert count_in_range(root, 5, 45) == 3
    print("All tests passed!")
