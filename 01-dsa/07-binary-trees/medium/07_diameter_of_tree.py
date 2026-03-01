"""
Diameter of Binary Tree

Day: 25 | Difficulty: Medium | Pattern: DFS / Height
LeetCode 543: https://leetcode.com/problems/diameter-of-binary-tree/

Problem:
    Given the root of a binary tree, return the length of the diameter of
    the tree. The diameter is the length of the longest path between any
    two nodes in the tree. This path may or may not pass through the root.

    The length of a path is the number of EDGES between nodes.

Examples:
    Input: root = [1,2,3,4,5]
           1
          / \
         2   3
        / \
       4   5
    Output: 3 (path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)

    Input: root = [1,2]
    Output: 1

Constraints:
    - The number of nodes in the tree is in the range [1, 10^4].
    - -100 <= Node.val <= 100

Hint:
    At each node, the longest path THROUGH that node = left_height + right_height.
    Track the maximum diameter seen so far using a variable outside the recursion.
    The height function returns the height but also updates the diameter.

Pattern: DFS Height with global tracking
Time: O(n)
Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode) -> int:
    """Return the diameter (longest path length in edges) of the binary tree."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,2,3,4,5] -> 3
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3)
    assert diameter_of_binary_tree(root1) == 3, (
        f"Test 1 failed: {diameter_of_binary_tree(root1)}"
    )

    # Test 2: [1,2] -> 1
    root2 = TreeNode(1, TreeNode(2))
    assert diameter_of_binary_tree(root2) == 1, f"Test 2 failed"

    # Test 3: Single node -> 0
    root3 = TreeNode(1)
    assert diameter_of_binary_tree(root3) == 0, f"Test 3 failed"

    # Test 4: Diameter doesn't pass through root
    #       1
    #      /
    #     2
    #    / \
    #   3   4
    #  /     \
    # 5       6
    # Diameter = 4 (5 -> 3 -> 2 -> 4 -> 6)
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3, TreeNode(5), None)
    root4.left.right = TreeNode(4, None, TreeNode(6))
    assert diameter_of_binary_tree(root4) == 4, (
        f"Test 4 failed: {diameter_of_binary_tree(root4)}"
    )

    print("All tests passed!")
