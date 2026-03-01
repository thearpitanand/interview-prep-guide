"""
Delete Node in a BST (LC 450)

Day: 27 | Difficulty: Medium | Pattern: BST Delete (3 Cases)

Given a root of a BST and a key, delete the node with the given key in the BST.
Return the root of the (possibly updated) BST.

The deletion can be broken down into 3 cases:
1. Node is a leaf: simply remove it.
2. Node has one child: replace node with its child.
3. Node has two children: replace with inorder successor (smallest in right
   subtree), then delete the successor from right subtree.

Examples:
    Input: root = [5,3,6,2,4,None,7], key = 3
    Output: [5,4,6,2,None,None,7]
    Explanation: Node 3 has two children. Replace with inorder successor (4),
                 then delete 4 from original position.

    Input: root = [5,3,6,2,4,None,7], key = 0
    Output: [5,3,6,2,4,None,7] (key not in tree, no change)

Constraints:
    - Number of nodes in the tree is in range [0, 10^4]
    - -10^5 <= Node.val <= 10^5
    - Each node has a unique value
    - root is a valid BST
    - -10^5 <= key <= 10^5

Hint:
    First find the node. Then handle the 3 cases:
    - Leaf: return None
    - One child: return the non-None child
    - Two children: find inorder successor (go right once, then left as far
      as possible), copy its value, then recursively delete the successor.

Pattern: BST Delete - find the node using BST property, then handle 3 cases.
The two-children case is the trickiest.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """Delete node with given key from BST and return new root."""
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


def inorder(root):
    """Get inorder traversal."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def search(root, val):
    """Search for a value in BST."""
    if not root:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Delete node with two children
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    result = delete_node(root, 3)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert not search(result, 3), "Node 3 still found after deletion"
    assert search(result, 2) and search(result, 4), "Other nodes should still exist"

    # Test 2: Delete leaf node
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    result = delete_node(root, 7)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert not search(result, 7), "Node 7 still found after deletion"

    # Test 3: Delete node with one child
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    result = delete_node(root, 6)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert not search(result, 6), "Node 6 still found after deletion"
    assert search(result, 7), "Node 7 should still exist"

    # Test 4: Delete root
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    result = delete_node(root, 5)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert not search(result, 5), "Node 5 still found after deletion"

    # Test 5: Key not in tree
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    original_inorder = inorder(root)
    result = delete_node(root, 0)
    assert inorder(result) == original_inorder, "Tree should not change when key not found"

    # Test 6: Delete from single node tree
    root = build_tree([5])
    result = delete_node(root, 5)
    assert result is None, "Expected None after deleting only node"

    print("All tests passed!")
