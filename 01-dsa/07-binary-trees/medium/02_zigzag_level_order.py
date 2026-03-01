"""
Binary Tree Zigzag Level Order Traversal

Day: 24 | Difficulty: Medium | Pattern: BFS
LeetCode 103: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Problem:
    Given the root of a binary tree, return the zigzag level order traversal
    of its nodes' values. (i.e., from left to right, then right to left for
    the next level and alternate between).

Examples:
    Input: root = [3,9,20,null,null,15,7]
         3           <- left to right
        / \
       9   20        <- right to left
          /  \
         15   7      <- left to right
    Output: [[3], [20, 9], [15, 7]]

    Input: root = [1]
    Output: [[1]]

    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 2000].
    - -100 <= Node.val <= 100

Hint:
    Same as level order, but reverse the level list on every other level.
    Use a flag (left_to_right) or check if the level index is odd/even.

Pattern: BFS Level Order with alternating direction
Time: O(n)
Space: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    """Return zigzag level order traversal as a list of lists."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert zigzag_level_order(root1) == [[3], [20, 9], [15, 7]], (
        f"Test 1 failed: {zigzag_level_order(root1)}"
    )

    # Test 2: [1] -> [[1]]
    root2 = TreeNode(1)
    assert zigzag_level_order(root2) == [[1]], "Test 2 failed"

    # Test 3: [] -> []
    assert zigzag_level_order(None) == [], "Test 3 failed"

    # Test 4: [1,2,3,4,5,6,7] -> [[1],[3,2],[4,5,6,7]]
    root4 = TreeNode(1)
    root4.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root4.right = TreeNode(3, TreeNode(6), TreeNode(7))
    assert zigzag_level_order(root4) == [[1], [3, 2], [4, 5, 6, 7]], (
        f"Test 4 failed: {zigzag_level_order(root4)}"
    )

    print("All tests passed!")
