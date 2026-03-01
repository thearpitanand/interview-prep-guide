"""
Subtree of Another Tree

Day: 23 | Difficulty: Easy | Pattern: DFS
LeetCode 572: https://leetcode.com/problems/subtree-of-another-tree/

Problem:
    Given the roots of two binary trees root and subRoot, return true if
    there is a subtree of root with the same structure and node values as
    subRoot, and false otherwise.

    A subtree of a binary tree is a tree that consists of a node and all
    of this node's descendants.

Examples:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
           3           4
          / \         / \
         4   5       1   2
        / \
       1   2
    Output: True

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: False (because the subtree has an extra node 0)

Constraints:
    - The number of nodes in root is in the range [1, 2000].
    - The number of nodes in subRoot is in the range [1, 1000].
    - -10^4 <= root.val, subRoot.val <= 10^4

Hint:
    For each node in root, check if the subtree starting at that node
    is identical to subRoot (reuse "same tree" logic).
    is_subtree(root, sub) = is_same(root, sub) OR is_subtree(root.left, sub)
                            OR is_subtree(root.right, sub)

Pattern: DFS + Same Tree check
Time: O(m * n) where m = nodes in root, n = nodes in subRoot
Space: O(h) where h = height of root
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: TreeNode, sub_root: TreeNode) -> bool:
    """Check if sub_root is a subtree of root."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [3,4,5,1,2] contains [4,1,2] -> True
    root1 = TreeNode(3)
    root1.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root1.right = TreeNode(5)
    sub1 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root1, sub1) is True, "Test 1 failed"

    # Test 2: [3,4,5,1,2,null,null,null,null,0] does NOT contain [4,1,2]
    root2 = TreeNode(3)
    root2.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root2.left.right.left = TreeNode(0)  # Extra node
    root2.right = TreeNode(5)
    sub2 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root2, sub2) is False, "Test 2 failed"

    # Test 3: Both single nodes with same value -> True
    assert is_subtree(TreeNode(1), TreeNode(1)) is True, "Test 3 failed"

    # Test 4: Both single nodes with different values -> False
    assert is_subtree(TreeNode(1), TreeNode(2)) is False, "Test 4 failed"

    # Test 5: subRoot is the entire root -> True
    root5 = TreeNode(1, TreeNode(2), TreeNode(3))
    sub5 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_subtree(root5, sub5) is True, "Test 5 failed"

    print("All tests passed!")
