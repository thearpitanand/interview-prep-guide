"""
Kth Smallest Element in a BST (LC 230)

Day: 26 | Difficulty: Medium | Pattern: Inorder Traversal

Given the root of a BST and an integer k, return the kth smallest value
(1-indexed) of all the values of the nodes in the tree.

Examples:
    Input: root = [3,1,4,None,2], k = 1
    Output: 1
    Explanation: Inorder traversal: [1, 2, 3, 4]. 1st smallest = 1.

    Input: root = [5,3,6,2,4,None,None,1], k = 3
    Output: 3
    Explanation: Inorder traversal: [1, 2, 3, 4, 5, 6]. 3rd smallest = 3.

Constraints:
    - Number of nodes in the tree is n
    - 1 <= k <= n <= 10^4
    - 0 <= Node.val <= 10^4

Hint:
    Inorder traversal of a BST gives elements in sorted (ascending) order.
    Perform inorder traversal and return the kth element. You can optimize
    by stopping early once k elements are visited (no need to traverse the
    entire tree).

Pattern: Inorder traversal with early termination. Use iterative approach
with stack for O(H + k) time where H is tree height.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """Return the kth smallest element in BST using iterative inorder."""
    pass


def kth_smallest_recursive(root: Optional[TreeNode], k: int) -> int:
    """Return the kth smallest element using recursive inorder."""
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
    # Test 1: k=1 (smallest element)
    root = build_tree([3, 1, 4, None, 2])
    assert kth_smallest(root, 1) == 1, f"Expected 1, got {kth_smallest(root, 1)}"

    # Test 2: k=3
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert kth_smallest(root, 3) == 3, f"Expected 3, got {kth_smallest(root, 3)}"

    # Test 3: k equals total nodes (largest element)
    root = build_tree([3, 1, 4, None, 2])
    assert kth_smallest(root, 4) == 4, f"Expected 4, got {kth_smallest(root, 4)}"

    # Test 4: Single node
    root = build_tree([1])
    assert kth_smallest(root, 1) == 1, f"Expected 1, got {kth_smallest(root, 1)}"

    # Test 5: Recursive approach
    root = build_tree([3, 1, 4, None, 2])
    assert kth_smallest_recursive(root, 1) == 1, f"Expected 1, got {kth_smallest_recursive(root, 1)}"

    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert kth_smallest_recursive(root, 3) == 3, f"Expected 3, got {kth_smallest_recursive(root, 3)}"

    print("All tests passed!")
