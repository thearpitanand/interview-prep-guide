"""
Problem: Find Median of BST O(n)/O(1) (GFG) | Optional | Hard
Topic: BST

Find the median of a BST in O(n) time and O(1) extra space (Morris Traversal).

Example 1:
  Input: BST = [5,3,7,2,4]
  Output: 4  # sorted: [2,3,4,5,7], median = 4

Constraints:
  - 1 <= n <= 10^5

Hint: First pass: count nodes. Second pass: Morris inorder to find middle element(s).
Pattern: Morris Traversal
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def median_bst(root: TreeNode) -> float:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
    assert median_bst(root) == 4
    print("All tests passed!")
