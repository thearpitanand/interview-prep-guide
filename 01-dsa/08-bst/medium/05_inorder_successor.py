"""
Inorder Successor in BST (LC 285 variant)

Day: 27 | Difficulty: Medium | Pattern: BST Property

Given a BST and a target node value, find the inorder successor of that node.
The inorder successor is the node with the smallest key greater than the
target node's value.

If the target node has no inorder successor, return None.

Examples:
    Input: root = [5,3,6,2,4,None,None,1], target = 3
    Output: 4
    Explanation: Inorder: [1,2,3,4,5,6]. Successor of 3 is 4.

    Input: root = [5,3,6,2,4,None,None,1], target = 6
    Output: None
    Explanation: 6 is the largest element; no successor exists.

    Input: root = [2,1,3], target = 1
    Output: 2

Constraints:
    - Number of nodes in the tree is in range [1, 10^4]
    - -10^5 <= Node.val <= 10^5
    - All values are unique
    - target value exists in the tree

Hint:
    Use BST property. Start from root. If target < current node, this node
    COULD be the successor (save it), then go left to find a smaller
    candidate. If target >= current node, go right (successor must be larger).

    Key insight: You don't need to find the target node first. Just track the
    last node where you turned LEFT -- that's your best successor candidate.

Pattern: BST Property - track the last "left turn" node as potential
successor while searching for the target.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_successor(root: Optional[TreeNode], target_val: int) -> Optional[TreeNode]:
    """Find the inorder successor of node with target_val in BST."""
    pass


def inorder_predecessor(root: Optional[TreeNode], target_val: int) -> Optional[TreeNode]:
    """Bonus: Find the inorder predecessor of node with target_val in BST."""
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
    # Test 1: Successor exists (middle of tree)
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    result = inorder_successor(root, 3)
    assert result is not None and result.val == 4, f"Expected 4, got {result.val if result else None}"

    # Test 2: No successor (largest element)
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    result = inorder_successor(root, 6)
    assert result is None, f"Expected None, got {result.val if result else None}"

    # Test 3: Successor is root
    root = build_tree([2, 1, 3])
    result = inorder_successor(root, 1)
    assert result is not None and result.val == 2, f"Expected 2, got {result.val if result else None}"

    # Test 4: Successor is parent's parent
    root = build_tree([20, 10, 30, 5, 15, 25, 35])
    result = inorder_successor(root, 15)
    assert result is not None and result.val == 20, f"Expected 20, got {result.val if result else None}"

    # Test 5: Successor of smallest element
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    result = inorder_successor(root, 1)
    assert result is not None and result.val == 2, f"Expected 2, got {result.val if result else None}"

    # Test 6: Predecessor
    root = build_tree([5, 3, 6, 2, 4])
    result = inorder_predecessor(root, 5)
    assert result is not None and result.val == 4, f"Expected 4, got {result.val if result else None}"

    result = inorder_predecessor(root, 2)
    assert result is None, f"Expected None for predecessor of smallest, got {result.val if result else None}"

    print("All tests passed!")
