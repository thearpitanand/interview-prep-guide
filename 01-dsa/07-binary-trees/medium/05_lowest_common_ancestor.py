"""
Lowest Common Ancestor of a Binary Tree

Day: 24 | Difficulty: Medium | Pattern: DFS / LCA
LeetCode 236: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Problem:
    Given a binary tree, find the lowest common ancestor (LCA) of two given
    nodes in the tree.

    The lowest common ancestor is defined as the lowest node in T that has
    both p and q as descendants (a node can be a descendant of itself).

Examples:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
              3
             / \
            5   1
           / \ / \
          6  2 0  8
            / \
           7   4
    Output: 3

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5 (a node can be its own ancestor)

Constraints:
    - The number of nodes in the tree is in the range [2, 10^5].
    - All Node.val are unique.
    - p != q
    - p and q will exist in the tree.

Hint:
    Recursively search left and right subtrees for p and q.
    - If current node is p or q, return it.
    - If both left and right return non-None, current node is LCA.
    - If only one side returns non-None, the LCA is on that side.

Pattern: LCA (post-order DFS)
Time: O(n)
Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Find the lowest common ancestor of nodes p and q."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Build the tree: [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Test 1: LCA(5, 1) = 3
    p1 = root.left       # node 5
    q1 = root.right      # node 1
    result1 = lowest_common_ancestor(root, p1, q1)
    assert result1.val == 3, f"Test 1 failed: expected 3, got {result1.val}"

    # Test 2: LCA(5, 4) = 5
    p2 = root.left                  # node 5
    q2 = root.left.right.right      # node 4
    result2 = lowest_common_ancestor(root, p2, q2)
    assert result2.val == 5, f"Test 2 failed: expected 5, got {result2.val}"

    # Test 3: LCA(6, 4) = 5
    p3 = root.left.left             # node 6
    q3 = root.left.right.right      # node 4
    result3 = lowest_common_ancestor(root, p3, q3)
    assert result3.val == 5, f"Test 3 failed: expected 5, got {result3.val}"

    # Test 4: LCA(7, 8) = 3
    p4 = root.left.right.left       # node 7
    q4 = root.right.right           # node 8
    result4 = lowest_common_ancestor(root, p4, q4)
    assert result4.val == 3, f"Test 4 failed: expected 3, got {result4.val}"

    print("All tests passed!")
