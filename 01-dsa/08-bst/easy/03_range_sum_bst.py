"""
Range Sum of BST (LC 938)

Day: 26 | Difficulty: Easy | Pattern: DFS with BST Property

Given the root of a BST and two integers low and high, return the sum of
values of all nodes with a value in the inclusive range [low, high].

Examples:
    Input: root = [10,5,15,3,7,None,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in range [7, 15]. Sum = 32.

    Input: root = [10,5,15,3,7,13,18,1,None,6], low = 6, high = 10
    Output: 23
    Explanation: Nodes 6, 7, and 10 are in range [6, 10]. Sum = 23.

Constraints:
    - Number of nodes in the tree is in range [1, 2 * 10^4]
    - 1 <= Node.val <= 10^5
    - 1 <= low <= high <= 10^5

Hint:
    Use BST property to prune branches. If current node's value < low, skip
    the entire left subtree. If current node's value > high, skip the entire
    right subtree.

Pattern: DFS with BST property-based pruning. Only explore subtrees that
could contain values in the given range.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root: TreeNode, low: int, high: int) -> int:
    """Return sum of all node values within [low, high] range."""
    pass


# --- Helper Functions ---

def build_bst(values):
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
    # Test 1: Standard range
    root = build_bst([10, 5, 15, 3, 7, None, 18])
    assert range_sum_bst(root, 7, 15) == 32, f"Expected 32, got {range_sum_bst(root, 7, 15)}"

    # Test 2: Wider range
    root = build_bst([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    assert range_sum_bst(root, 6, 10) == 23, f"Expected 23, got {range_sum_bst(root, 6, 10)}"

    # Test 3: Single node in range
    root = build_bst([10, 5, 15])
    assert range_sum_bst(root, 10, 10) == 10, f"Expected 10, got {range_sum_bst(root, 10, 10)}"

    # Test 4: All nodes in range
    root = build_bst([10, 5, 15])
    assert range_sum_bst(root, 1, 20) == 30, f"Expected 30, got {range_sum_bst(root, 1, 20)}"

    # Test 5: No nodes in range
    root = build_bst([10, 5, 15])
    assert range_sum_bst(root, 11, 14) == 0, f"Expected 0, got {range_sum_bst(root, 11, 14)}"

    print("All tests passed!")
