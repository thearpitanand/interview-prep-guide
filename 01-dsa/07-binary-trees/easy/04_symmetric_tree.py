"""
Symmetric Tree

Day: 23 | Difficulty: Easy | Pattern: DFS
LeetCode 101: https://leetcode.com/problems/symmetric-tree/

Problem:
    Given the root of a binary tree, check whether it is a mirror of itself
    (i.e., symmetric around its center).

Examples:
    Input: root = [1,2,2,3,4,4,3]
           1
          / \
         2   2
        / \ / \
       3  4 4  3
    Output: True

    Input: root = [1,2,2,null,3,null,3]
           1
          / \
         2   2
          \   \
           3   3
    Output: False

Constraints:
    - The number of nodes in the tree is in the range [1, 1000].
    - -100 <= Node.val <= 100

Hint:
    A tree is symmetric if the left subtree is a mirror of the right subtree.
    Use a helper function that compares two nodes:
    - Both None -> True
    - One None -> False
    - Values equal AND mirror(left.left, right.right) AND mirror(left.right, right.left)

Pattern: DFS Recursive (mirror comparison)
Time: O(n)
Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    """Check if the binary tree is symmetric (mirror of itself)."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,2,2,3,4,4,3] -> True
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))
    assert is_symmetric(root1) is True, "Test 1 failed"

    # Test 2: [1,2,2,null,3,null,3] -> False
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))
    assert is_symmetric(root2) is False, "Test 2 failed"

    # Test 3: Single node -> True
    root3 = TreeNode(1)
    assert is_symmetric(root3) is True, "Test 3 failed"

    # Test 4: [1,2,2] -> True
    root4 = TreeNode(1, TreeNode(2), TreeNode(2))
    assert is_symmetric(root4) is True, "Test 4 failed"

    print("All tests passed!")
