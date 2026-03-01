"""
Count Complete Tree Nodes

Day: 25 | Difficulty: Medium | Pattern: Binary Search + DFS
LeetCode 222: https://leetcode.com/problems/count-complete-tree-nodes/

Problem:
    Given the root of a complete binary tree, return the number of nodes.
    Design an algorithm that runs in less than O(n) time complexity.

    A complete binary tree is one where every level except possibly the last
    is completely filled, and all nodes in the last level are as far left
    as possible.

Examples:
    Input: root = [1,2,3,4,5,6]
           1
          / \
         2   3
        / \ /
       4  5 6
    Output: 6

    Input: root = []
    Output: 0

    Input: root = [1]
    Output: 1

Constraints:
    - The number of nodes in the tree is in the range [0, 5 * 10^4].
    - 0 <= Node.val <= 5 * 10^4
    - The tree is guaranteed to be complete.

Hint:
    For a complete tree, compare left height and right height:
    - If left_height == right_height: left subtree is a perfect binary tree
      with 2^left_height - 1 nodes. Recurse on right subtree.
    - If left_height != right_height: right subtree is a perfect binary tree
      with 2^right_height - 1 nodes. Recurse on left subtree.
    This gives O(log^2 n) time.

Pattern: Binary Search + DFS (exploiting complete tree property)
Time: O(log^2 n) - log n levels, each height computation is O(log n)
Space: O(log n) - recursion depth
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root: TreeNode) -> int:
    """Count nodes in a complete binary tree in O(log^2 n) time."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,2,3,4,5,6] -> 6
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3, TreeNode(6), None)
    assert count_nodes(root1) == 6, f"Test 1 failed: {count_nodes(root1)}"

    # Test 2: [] -> 0
    assert count_nodes(None) == 0, "Test 2 failed"

    # Test 3: [1] -> 1
    assert count_nodes(TreeNode(1)) == 1, "Test 3 failed"

    # Test 4: Perfect tree [1,2,3,4,5,6,7] -> 7
    root4 = TreeNode(1)
    root4.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root4.right = TreeNode(3, TreeNode(6), TreeNode(7))
    assert count_nodes(root4) == 7, f"Test 4 failed: {count_nodes(root4)}"

    # Test 5: [1,2,3] -> 3
    root5 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert count_nodes(root5) == 3, f"Test 5 failed: {count_nodes(root5)}"

    # Test 6: [1,2] -> 2
    root6 = TreeNode(1, TreeNode(2))
    assert count_nodes(root6) == 2, f"Test 6 failed: {count_nodes(root6)}"

    print("All tests passed!")
