"""
Maximum Width of Binary Tree

Day: 25 | Difficulty: Hard | Pattern: BFS
LeetCode 662: https://leetcode.com/problems/maximum-width-of-binary-tree/

Problem:
    Given the root of a binary tree, return the maximum width of the given
    tree. The maximum width is the maximum width among all levels.

    The width of one level is defined as the length between the leftmost and
    rightmost non-null nodes, where the null nodes between them are also
    counted into the length calculation.

Examples:
    Input: root = [1,3,2,5,3,null,9]
               1
              / \
             3   2
            / \   \
           5   3   9
    Output: 4 (width of level 2: from node 5 to node 9, positions 0-3)

    Input: root = [1,3,2,5,null,null,9,6,null,7]
    Output: 7

    Input: root = [1,3,2,5]
    Output: 2

Constraints:
    - The number of nodes in the tree is in the range [1, 3000].
    - -100 <= Node.val <= 100

Hint:
    Assign position indices to each node: root = 0, left child = 2*pos,
    right child = 2*pos + 1 (like a heap). Width at a level =
    rightmost_position - leftmost_position + 1.

    Use BFS with (node, position) tuples. At each level, width =
    last_position - first_position + 1.

    To avoid integer overflow in very deep trees, normalize positions at
    each level by subtracting the first position.

Pattern: BFS with position indexing
Time: O(n)
Space: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def width_of_binary_tree(root: TreeNode) -> int:
    """Return the maximum width of the binary tree."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,3,2,5,3,null,9] -> 4
    root1 = TreeNode(1)
    root1.left = TreeNode(3, TreeNode(5), TreeNode(3))
    root1.right = TreeNode(2, None, TreeNode(9))
    assert width_of_binary_tree(root1) == 4, (
        f"Test 1 failed: {width_of_binary_tree(root1)}"
    )

    # Test 2: [1,3,2,5] -> 2
    root2 = TreeNode(1)
    root2.left = TreeNode(3, TreeNode(5), None)
    root2.right = TreeNode(2)
    assert width_of_binary_tree(root2) == 2, (
        f"Test 2 failed: {width_of_binary_tree(root2)}"
    )

    # Test 3: Single node -> 1
    assert width_of_binary_tree(TreeNode(1)) == 1, "Test 3 failed"

    # Test 4: [1,1,1,1,null,null,1,1,null,null,1]
    #          1                  width=1
    #         / \
    #        1   1               width=2
    #       /     \
    #      1       1             width=4 (positions 0 and 3)
    #     /         \
    #    1           1           width=8 (positions 0 and 7)
    root4 = TreeNode(1)
    root4.left = TreeNode(1, TreeNode(1, TreeNode(1), None), None)
    root4.right = TreeNode(1, None, TreeNode(1, None, TreeNode(1)))
    assert width_of_binary_tree(root4) == 8, (
        f"Test 4 failed: {width_of_binary_tree(root4)}"
    )

    # Test 5: Complete tree [1,2,3,4,5,6,7] -> 4
    root5 = TreeNode(1)
    root5.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root5.right = TreeNode(3, TreeNode(6), TreeNode(7))
    assert width_of_binary_tree(root5) == 4, (
        f"Test 5 failed: {width_of_binary_tree(root5)}"
    )

    print("All tests passed!")
