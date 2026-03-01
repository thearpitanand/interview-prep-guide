"""
Serialize and Deserialize BST (LC 449)

Day: 27 | Difficulty: Hard | Pattern: BST Property (Preorder)

Design an algorithm to serialize and deserialize a BST. Serialization is
converting a data structure to a string. Deserialization is reconstructing
the data structure from the string.

The encoded string should be as compact as possible.

Note: This is different from LC 297 (general binary tree) because we can
leverage the BST property for a more compact encoding. For a BST, preorder
traversal alone is sufficient to reconstruct the tree (no need for null
markers).

Examples:
    Input: root = [2,1,3]
    Serialize: "2,1,3" (preorder)
    Deserialize back to: [2,1,3]

    Input: root = []
    Serialize: ""
    Deserialize: None

Constraints:
    - Number of nodes in the tree is in range [0, 10^4]
    - 0 <= Node.val <= 10^4
    - The input tree is guaranteed to be a BST

Hint:
    Serialize: Use preorder traversal (root, left, right). No need for null
    markers since BST property lets us reconstruct the structure.

    Deserialize: Use the preorder sequence with bounds. For each value, check
    if it falls within the valid range. If yes, create a node. If no, return
    None (backtrack).

    Key insight: In a BST, preorder traversal uniquely determines the tree.
    For general binary trees, you need preorder + inorder (or null markers).

Pattern: BST Property with Preorder traversal. Serialize without null markers.
Deserialize by maintaining valid ranges for each position.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """Codec for serializing and deserializing BST."""

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encode BST to a single string."""
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decode string back to BST."""
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
    codec = Codec()

    # Test 1: Standard BST
    root = build_tree([2, 1, 3])
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert tree_to_list(deserialized) == [2, 1, 3], f"Expected [2,1,3], got {tree_to_list(deserialized)}"
    assert is_valid_bst(deserialized), "Deserialized tree is not a valid BST"

    # Test 2: Empty tree
    serialized = codec.serialize(None)
    deserialized = codec.deserialize(serialized)
    assert deserialized is None, f"Expected None for empty tree"

    # Test 3: Single node
    root = build_tree([5])
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert tree_to_list(deserialized) == [5], f"Expected [5], got {tree_to_list(deserialized)}"

    # Test 4: Larger BST
    root = build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13])
    original_inorder = inorder(root)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert is_valid_bst(deserialized), "Deserialized tree is not a valid BST"
    assert inorder(deserialized) == original_inorder, f"Inorder mismatch: {inorder(deserialized)} vs {original_inorder}"

    # Test 5: No null markers needed (compact)
    root = build_tree([4, 2, 6, 1, 3, 5, 7])
    serialized = codec.serialize(root)
    # Verify compactness: no null/None markers in serialized string
    assert "null" not in serialized.lower() and "none" not in serialized.lower(), \
        f"Serialized string should not contain null markers: {serialized}"

    # Test 6: Roundtrip preserves structure
    root = build_tree([10, 5, 15, 3, 7, 12, 20])
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert tree_to_list(deserialized) == tree_to_list(root), \
        f"Roundtrip failed: {tree_to_list(deserialized)} vs {tree_to_list(root)}"

    print("All tests passed!")
