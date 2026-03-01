"""
Maximum Depth of Binary Tree

Day: 23 | Difficulty: Easy | Pattern: DFS / Height
LeetCode 104: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem:
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest
    path from the root node down to the farthest leaf node.

Examples:
    Input: root = [3, 9, 20, null, null, 15, 7]
         3
        / \
       9   20
          /  \
         15   7
    Output: 3

    Input: root = [1, null, 2]
    Output: 2

Constraints:
    - The number of nodes in the tree is in the range [0, 10^4].
    - -100 <= Node.val <= 100

Hint:
    The max depth of a tree = 1 + max(depth of left subtree, depth of right subtree).
    Base case: empty node has depth 0.

Pattern: DFS Height/Depth
Time: O(n) - visit every node
Space: O(h) - recursion stack, where h is the height
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """Return the maximum depth of the binary tree."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [3,9,20,null,null,15,7] -> 3
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert max_depth(root1) == 3, f"Test 1 failed: {max_depth(root1)}"

    # Test 2: [1, null, 2] -> 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    assert max_depth(root2) == 2, f"Test 2 failed: {max_depth(root2)}"

    # Test 3: [] -> 0
    assert max_depth(None) == 0, f"Test 3 failed: {max_depth(None)}"

    # Test 4: [1] -> 1
    root4 = TreeNode(1)
    assert max_depth(root4) == 1, f"Test 4 failed: {max_depth(root4)}"

    # Test 5: Left-skewed [1,2,null,3] -> 3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    assert max_depth(root5) == 3, f"Test 5 failed: {max_depth(root5)}"

    print("All tests passed!")
