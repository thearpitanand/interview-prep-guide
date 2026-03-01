"""
Validate Binary Search Tree (LC 98)

Day: 26 | Difficulty: Medium | Pattern: DFS with Range

Given the root of a binary tree, determine if it is a valid BST.

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be BSTs.

Examples:
    Input: root = [2,1,3]
    Output: True

    Input: root = [5,1,4,None,None,3,6]
    Output: False
    Explanation: The root's right child is 4, which is less than root (5).

Constraints:
    - Number of nodes in the tree is in range [1, 10^4]
    - -2^31 <= Node.val <= 2^31 - 1

Hint:
    Don't just check left < root < right for immediate children. A node in the
    left subtree must be less than ALL ancestors above it. Pass a valid range
    (low, high) down the recursion.

    Common mistake: Only checking node.left.val < node.val < node.right.val.
    This fails for cases like [5,4,6,None,None,3,7] where 3 is in right
    subtree of 5 but 3 < 5.

Pattern: DFS with Range - pass (low, high) bounds down. Each node must be
within its allowed range.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Determine if the binary tree is a valid BST using range-based validation."""
    pass


def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    """Alternative approach: inorder traversal should produce strictly increasing sequence."""
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


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Valid BST
    root = build_tree([2, 1, 3])
    assert is_valid_bst(root) == True, "Expected True for [2,1,3]"

    # Test 2: Invalid BST - right child less than root
    root = build_tree([5, 1, 4, None, None, 3, 6])
    assert is_valid_bst(root) == False, "Expected False for [5,1,4,None,None,3,6]"

    # Test 3: Single node
    root = build_tree([1])
    assert is_valid_bst(root) == True, "Expected True for single node"

    # Test 4: Tricky case - node violates ancestor constraint
    # Node 3 is in right subtree of 5 but 3 < 5
    root = build_tree([5, 4, 6, None, None, 3, 7])
    assert is_valid_bst(root) == False, "Expected False for [5,4,6,None,None,3,7]"

    # Test 5: Equal values (not valid in strict BST)
    root = build_tree([2, 2, 2])
    assert is_valid_bst(root) == False, "Expected False for equal values"

    # Test 6: Inorder approach
    root = build_tree([2, 1, 3])
    assert is_valid_bst_inorder(root) == True, "Inorder: Expected True for [2,1,3]"

    root = build_tree([5, 1, 4, None, None, 3, 6])
    assert is_valid_bst_inorder(root) == False, "Inorder: Expected False for [5,1,4,None,None,3,6]"

    print("All tests passed!")
