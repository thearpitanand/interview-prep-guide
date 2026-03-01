"""
Balanced Binary Tree

Day: 25 | Difficulty: Medium | Pattern: DFS / Height
LeetCode 110: https://leetcode.com/problems/balanced-binary-tree/

Problem:
    Given a binary tree, determine if it is height-balanced.
    A height-balanced binary tree is a binary tree in which the depth of
    the two subtrees of every node never differs by more than one.

Examples:
    Input: root = [3,9,20,null,null,15,7]
         3
        / \
       9   20
          /  \
         15   7
    Output: True

    Input: root = [1,2,2,3,3,null,null,4,4]
           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Output: False

    Input: root = []
    Output: True

Constraints:
    - The number of nodes in the tree is in the range [0, 5000].
    - -10^4 <= Node.val <= 10^4

Hint:
    Use a height function that returns -1 if the subtree is unbalanced.
    At each node: if left or right subtree is unbalanced (-1), propagate -1.
    If abs(left_height - right_height) > 1, return -1.
    Otherwise return 1 + max(left, right).

Pattern: DFS Height with early termination
Time: O(n)
Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode) -> bool:
    """Check if the binary tree is height-balanced."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [3,9,20,null,null,15,7] -> True
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert is_balanced(root1) is True, "Test 1 failed"

    # Test 2: [1,2,2,3,3,null,null,4,4] -> False
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
    root2.right = TreeNode(2)
    assert is_balanced(root2) is False, "Test 2 failed"

    # Test 3: [] -> True
    assert is_balanced(None) is True, "Test 3 failed"

    # Test 4: [1] -> True
    assert is_balanced(TreeNode(1)) is True, "Test 4 failed"

    # Test 5: Right-skewed [1,null,2,null,3] -> False
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    assert is_balanced(root5) is False, "Test 5 failed"

    print("All tests passed!")
