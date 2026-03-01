"""
Binary Tree Right Side View

Day: 24 | Difficulty: Medium | Pattern: BFS
LeetCode 199: https://leetcode.com/problems/binary-tree-right-side-view/

Problem:
    Given the root of a binary tree, imagine yourself standing on the right
    side of it, return the values of the nodes you can see ordered from top
    to bottom.

Examples:
    Input: root = [1,2,3,null,5,null,4]
           1        <-- you see 1
          / \
         2   3      <-- you see 3
          \   \
           5   4    <-- you see 4
    Output: [1, 3, 4]

    Input: root = [1,null,3]
    Output: [1, 3]

    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 100].
    - -100 <= Node.val <= 100

Hint:
    Use BFS (level order traversal). The rightmost node at each level is the
    one visible from the right side. That's the last node processed in each
    level of the BFS.

Pattern: BFS Level Order (last node per level)
Time: O(n)
Space: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> list[int]:
    """Return the right side view of the binary tree."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,2,3,null,5,null,4] -> [1,3,4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, None, TreeNode(5))
    root1.right = TreeNode(3, None, TreeNode(4))
    assert right_side_view(root1) == [1, 3, 4], f"Test 1 failed: {right_side_view(root1)}"

    # Test 2: [1,null,3] -> [1,3]
    root2 = TreeNode(1, None, TreeNode(3))
    assert right_side_view(root2) == [1, 3], f"Test 2 failed"

    # Test 3: [] -> []
    assert right_side_view(None) == [], "Test 3 failed"

    # Test 4: [1] -> [1]
    assert right_side_view(TreeNode(1)) == [1], "Test 4 failed"

    # Test 5: Left side deeper -> [1,2,4]
    #     1
    #    /
    #   2
    #  /
    # 4
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(4)
    assert right_side_view(root5) == [1, 2, 4], f"Test 5 failed: {right_side_view(root5)}"

    print("All tests passed!")
