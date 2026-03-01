"""
Lowest Common Ancestor of a Binary Search Tree (LC 235)

Day: 27 | Difficulty: Medium | Pattern: BST Property

Given a BST, find the lowest common ancestor (LCA) of two given nodes.

The LCA is defined as the lowest node in the tree that has both p and q as
descendants (where a node can be a descendant of itself).

Examples:
    Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8
    Output: 6
    Explanation: LCA of 2 and 8 is 6 (root), since 2 is in left subtree
                 and 8 is in right subtree.

    Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 4
    Output: 2
    Explanation: LCA of 2 and 4 is 2, since 4 is a descendant of 2.

    Input: root = [2,1], p = 2, q = 1
    Output: 2

Constraints:
    - Number of nodes in the tree is in range [2, 10^5]
    - -10^9 <= Node.val <= 10^9
    - All Node.val are unique
    - p != q
    - p and q exist in the BST

Hint:
    Use the BST property! If both p and q are smaller than current node, LCA
    must be in left subtree. If both are larger, LCA must be in right subtree.
    If they split (one left, one right), current node IS the LCA.

    This is O(h) vs O(n) for the general binary tree LCA approach.

Pattern: BST Property - the split point where p and q go to different
subtrees is the LCA. Much simpler than general tree LCA.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Find LCA of p and q in BST using BST property."""
    pass


def lowest_common_ancestor_iterative(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Iterative approach - O(1) space."""
    pass


# --- Helper Functions ---

def build_tree(values):
    """Build a binary tree from a level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def find_node(root, val):
    """Find a node by value in BST."""
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return find_node(root.left, val)
    return find_node(root.right, val)


# --- Tests ---

if __name__ == "__main__":
    # Test 1: LCA is root (p and q on different sides)
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 8)
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 6, f"Expected 6, got {result.val}"

    # Test 2: LCA is one of the nodes (ancestor relationship)
    p = find_node(root, 2)
    q = find_node(root, 4)
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 2, f"Expected 2, got {result.val}"

    # Test 3: Nodes in right subtree
    p = find_node(root, 7)
    q = find_node(root, 9)
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 8, f"Expected 8, got {result.val}"

    # Test 4: Leaf nodes
    p = find_node(root, 3)
    q = find_node(root, 5)
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 4, f"Expected 4, got {result.val}"

    # Test 5: Simple tree
    root = build_tree([2, 1])
    p = find_node(root, 2)
    q = find_node(root, 1)
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 2, f"Expected 2, got {result.val}"

    # Test 6: Iterative approach
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 8)
    result = lowest_common_ancestor_iterative(root, p, q)
    assert result.val == 6, f"Iterative: Expected 6, got {result.val}"

    print("All tests passed!")
