"""
Recover Binary Search Tree (LC 99)

Day: 27 | Difficulty: Hard | Pattern: Inorder Traversal

You are given the root of a BST where the values of exactly two nodes have
been swapped by mistake. Recover the tree without changing its structure.

Examples:
    Input: root = [1,3,None,None,2]
    Output: [3,1,None,None,2]
    Explanation: 1 and 3 were swapped. 3 should be root, 1 should be left child.

    Input: root = [3,1,4,None,None,2]
    Output: [2,1,4,None,None,3]
    Explanation: 2 and 3 were swapped.

Constraints:
    - Number of nodes in the tree is in range [2, 1000]
    - -2^31 <= Node.val <= 2^31 - 1

Hint:
    Inorder traversal of a valid BST is strictly increasing. If two nodes are
    swapped, there will be one or two "inversions" (places where the sequence
    decreases).

    Case 1 - Adjacent swap: One inversion. E.g., [1,3,2,4] - first node of
    the inversion (3) and second node (2) are the swapped pair.

    Case 2 - Non-adjacent swap: Two inversions. E.g., [1,4,3,2,5] - first
    node of FIRST inversion (4) and second node of SECOND inversion (2) are
    the swapped pair.

    Follow-up: Can you solve it in O(1) space? (Morris traversal)

Pattern: Inorder traversal to detect inversions. Track first and second
nodes that are out of order, then swap their values.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recover_tree(root: Optional[TreeNode]) -> None:
    """Recover BST by finding and swapping the two misplaced nodes. Modifies tree in-place."""
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


def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    """Check if tree is a valid BST."""
    if not root:
        return True
    if root.val <= low or root.val >= high:
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)


def tree_to_list(root):
    """Convert tree to level-order list."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def inorder(root):
    """Get inorder traversal."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Swap in left subtree (adjacent in inorder)
    root = build_tree([1, 3, None, None, 2])
    recover_tree(root)
    assert is_valid_bst(root), f"Not valid BST. Inorder: {inorder(root)}"
    assert tree_to_list(root) == [3, 1, None, None, 2], f"Expected [3,1,None,None,2], got {tree_to_list(root)}"

    # Test 2: Non-adjacent swap
    root = build_tree([3, 1, 4, None, None, 2])
    recover_tree(root)
    assert is_valid_bst(root), f"Not valid BST. Inorder: {inorder(root)}"
    assert tree_to_list(root) == [2, 1, 4, None, None, 3], f"Expected [2,1,4,None,None,3], got {tree_to_list(root)}"

    # Test 3: Two nodes swapped
    root = build_tree([2, 3, 1])  # 1 and 3 swapped
    recover_tree(root)
    assert is_valid_bst(root), f"Not valid BST. Inorder: {inorder(root)}"

    # Test 4: Larger tree
    root = build_tree([6, 3, 8, 1, 4, 7, 9])  # Valid BST first
    # Swap 3 and 7
    root.left.val, root.right.left.val = root.right.left.val, root.left.val
    recover_tree(root)
    assert is_valid_bst(root), f"Not valid BST. Inorder: {inorder(root)}"
    assert inorder(root) == [1, 3, 4, 6, 7, 8, 9], f"Unexpected inorder: {inorder(root)}"

    print("All tests passed!")
