"""
Vertical Order Traversal of a Binary Tree

Day: 25 | Difficulty: Hard | Pattern: BFS + Sort
LeetCode 987: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Problem:
    Given the root of a binary tree, calculate the vertical order traversal
    of the binary tree.

    For each node at position (row, col):
    - Its left child is at (row + 1, col - 1)
    - Its right child is at (row + 1, col + 1)
    - The root is at (0, 0)

    The vertical order traversal returns a list of top-to-bottom orderings
    for each column index, sorted from leftmost column to rightmost.
    If two nodes are in the same row and column, sort them by value.

Examples:
    Input: root = [3,9,20,null,null,15,7]
         3          col: 0
        / \
       9   20       col: -1, 1
          /  \
         15   7     col: 0, 2
    Output: [[9], [3, 15], [20], [7]]

    Input: root = [1,2,3,4,5,6,7]
    Output: [[4], [2], [1, 5, 6], [3], [7]]

Constraints:
    - The number of nodes in the tree is in the range [1, 1000].
    - 0 <= Node.val <= 1000

Hint:
    Use BFS with (node, row, col) tuples in the queue.
    Collect all (row, col, val) tuples, then sort by (col, row, val).
    Group by column for the final result.

    Alternative: Use a defaultdict keyed by column, storing (row, val) pairs.

Pattern: BFS + Column/Row tracking + Sort
Time: O(n log n) due to sorting
Space: O(n)
"""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root: TreeNode) -> list[list[int]]:
    """Return the vertical order traversal of the binary tree."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [3,9,20,null,null,15,7] -> [[9],[3,15],[20],[7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert vertical_traversal(root1) == [[9], [3, 15], [20], [7]], (
        f"Test 1 failed: {vertical_traversal(root1)}"
    )

    # Test 2: [1,2,3,4,5,6,7] -> [[4],[2],[1,5,6],[3],[7]]
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root2.right = TreeNode(3, TreeNode(6), TreeNode(7))
    assert vertical_traversal(root2) == [[4], [2], [1, 5, 6], [3], [7]], (
        f"Test 2 failed: {vertical_traversal(root2)}"
    )

    # Test 3: Single node [1] -> [[1]]
    assert vertical_traversal(TreeNode(1)) == [[1]], "Test 3 failed"

    # Test 4: [3,1,4,0,2,2]
    # Same row+col nodes sorted by value:
    #       3        col 0
    #      / \
    #     1   4      col -1, 1
    #    / \ /
    #   0  2 2       col -2, 0, 0
    root4 = TreeNode(3)
    root4.left = TreeNode(1, TreeNode(0), TreeNode(2))
    root4.right = TreeNode(4, TreeNode(2), None)
    # col -2: [0], col -1: [1], col 0: [3, 2, 2], col 1: [4]
    result4 = vertical_traversal(root4)
    assert result4 == [[0], [1], [3, 2, 2], [4]], (
        f"Test 4 failed: {result4}"
    )

    print("All tests passed!")
