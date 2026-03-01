"""
Binary Tree Maximum Path Sum

Day: 25 | Difficulty: Hard | Pattern: DFS / Path + Height
LeetCode 124: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem:
    A path in a binary tree is a sequence of nodes where each pair of
    adjacent nodes has an edge connecting them. A node can only appear in
    the path at most once. The path does NOT need to pass through the root.

    Given the root of a binary tree, return the maximum path sum of any
    non-empty path.

Examples:
    Input: root = [1,2,3]
       1
      / \
     2   3
    Output: 6 (path: 2 -> 1 -> 3)

    Input: root = [-10,9,20,null,null,15,7]
        -10
        / \
       9   20
          /  \
         15   7
    Output: 42 (path: 15 -> 20 -> 7)

Constraints:
    - The number of nodes in the tree is in the range [1, 3 * 10^4].
    - -1000 <= Node.val <= 1000

Hint:
    At each node, compute the max "gain" from that node going down one side.
    The gain = node.val + max(left_gain, right_gain), but clamp to 0 if negative.
    The max path THROUGH a node = node.val + left_gain + right_gain.
    Track the global maximum across all nodes.

    Key insight: The recursive function returns the max gain going DOWN
    (single path), but we track the max path sum THROUGH each node
    (potentially using both sides) in a global variable.

Pattern: DFS with global max tracking
Time: O(n)
Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    """Return the maximum path sum in the binary tree."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,2,3] -> 6
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert max_path_sum(root1) == 6, f"Test 1 failed: {max_path_sum(root1)}"

    # Test 2: [-10,9,20,null,null,15,7] -> 42
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert max_path_sum(root2) == 42, f"Test 2 failed: {max_path_sum(root2)}"

    # Test 3: Single node [-3] -> -3
    root3 = TreeNode(-3)
    assert max_path_sum(root3) == -3, f"Test 3 failed: {max_path_sum(root3)}"

    # Test 4: All negative [-10,-20,-30] -> -10
    root4 = TreeNode(-10, TreeNode(-20), TreeNode(-30))
    assert max_path_sum(root4) == -10, f"Test 4 failed: {max_path_sum(root4)}"

    # Test 5: [2,-1] -> 2
    root5 = TreeNode(2, TreeNode(-1))
    assert max_path_sum(root5) == 2, f"Test 5 failed: {max_path_sum(root5)}"

    # Test 6: Complex tree
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  / \       \
    # 7   2       1
    root6 = TreeNode(5)
    root6.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None)
    root6.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    assert max_path_sum(root6) == 48, f"Test 6 failed: {max_path_sum(root6)}"

    print("All tests passed!")
