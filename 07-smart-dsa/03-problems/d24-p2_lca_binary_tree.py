"""
Problem: Lowest Common Ancestor of a Binary Tree (LC 236) | Smart-DSA Day 24 | Medium
Pattern: Tree DFS
Time target: 30 minutes

Given a binary tree and two nodes p and q, find their lowest common ancestor
(LCA). The LCA is the deepest node that has both p and q as descendants
(a node can be a descendant of itself).

Example 1:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
  Output: 3

Example 2:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
  Output: 5  (p itself is the LCA)

Constraints:
  - The number of nodes is in [2, 10^5].
  - -10^9 <= Node.val <= 10^9
  - All values are unique.
  - p and q are different nodes that both exist in the tree.

Hint (⚠ read only after time budget is blown):
  Post-order DFS: return the node if it equals p or q. If both left and right
  children return non-None, the current node is the LCA. Otherwise bubble up
  whichever side returned non-None.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    pass


if __name__ == "__main__":
    # Build [3,5,1,6,2,0,8,null,null,7,4]
    n3 = TreeNode(3)
    n5 = TreeNode(5); n1 = TreeNode(1)
    n6 = TreeNode(6); n2 = TreeNode(2); n0 = TreeNode(0); n8 = TreeNode(8)
    n7 = TreeNode(7); n4 = TreeNode(4)
    n3.left = n5; n3.right = n1
    n5.left = n6; n5.right = n2
    n1.left = n0; n1.right = n8
    n2.left = n7; n2.right = n4

    # LCA(5, 1) == 3
    assert lowest_common_ancestor(n3, n5, n1).val == 3

    # LCA(5, 4) == 5
    assert lowest_common_ancestor(n3, n5, n4).val == 5

    # LCA(6, 4) == 5
    assert lowest_common_ancestor(n3, n6, n4).val == 5

    print("All tests passed!")
