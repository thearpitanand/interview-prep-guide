"""
Problem: Kth Smallest Element in a BST (LC 230) | Smart-DSA Day 26 | Medium
Pattern: BST
Time target: 25 minutes

Given the root of a binary search tree and an integer k, return the kth
smallest value (1-indexed) of all the values in the tree.

Example 1:
  Input: root = [3,1,4,null,2], k = 1
  Output: 1

Example 2:
  Input: root = [5,3,6,2,4,null,null,1], k = 3
  Output: 3

Constraints:
  - The number of nodes is n where 1 <= k <= n <= 10^4.
  - 0 <= Node.val <= 10^4

Hint (⚠ read only after time budget is blown):
  In-order traversal visits BST nodes in ascending order. Count nodes as you
  visit them; stop and return when the counter reaches k. Use an iterative
  stack-based in-order to exit early without visiting the full tree.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode | None, k: int) -> int:
    pass


if __name__ == "__main__":
    # [3,1,4,null,2], k=1 -> 1
    root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert kth_smallest(root1, 1) == 1

    # [5,3,6,2,4,null,null,1], k=3 -> 3
    root2 = TreeNode(5,
                     TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                     TreeNode(6))
    assert kth_smallest(root2, 3) == 3

    # Single node, k=1
    assert kth_smallest(TreeNode(7), 1) == 7

    # k equals tree size
    root3 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert kth_smallest(root3, 3) == 3

    print("All tests passed!")
