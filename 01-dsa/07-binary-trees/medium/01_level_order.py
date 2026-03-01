"""
Binary Tree Level Order Traversal

Day: 24 | Difficulty: Medium | Pattern: BFS
LeetCode 102: https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem:
    Given the root of a binary tree, return the level order traversal of
    its nodes' values (i.e., from left to right, level by level).

Examples:
    Input: root = [3,9,20,null,null,15,7]
         3
        / \
       9   20
          /  \
         15   7
    Output: [[3], [9, 20], [15, 7]]

    Input: root = [1]
    Output: [[1]]

    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 2000].
    - -1000 <= Node.val <= 1000

Hint:
    Use a queue (deque). Process all nodes at the current level before
    moving to the next. The key trick: use len(queue) at the start of
    each level to know how many nodes belong to the current level.

Pattern: BFS Level Order (queue-based)
Time: O(n) - visit every node
Space: O(n) - queue can hold up to n/2 nodes (last level of complete tree)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> list[list[int]]:
    """Return level order traversal as a list of lists."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert level_order(root1) == [[3], [9, 20], [15, 7]], f"Test 1 failed: {level_order(root1)}"

    # Test 2: [1] -> [[1]]
    root2 = TreeNode(1)
    assert level_order(root2) == [[1]], f"Test 2 failed"

    # Test 3: [] -> []
    assert level_order(None) == [], f"Test 3 failed"

    # Test 4: [1,2,3,4,5] -> [[1],[2,3],[4,5]]
    root4 = TreeNode(1)
    root4.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root4.right = TreeNode(3)
    assert level_order(root4) == [[1], [2, 3], [4, 5]], f"Test 4 failed"

    print("All tests passed!")
