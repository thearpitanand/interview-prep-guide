"""
Minimum Absolute Difference in BST (LC 530)

Day: 26 | Difficulty: Easy | Pattern: Inorder Traversal

Given the root of a BST, return the minimum absolute difference between the
values of any two different nodes in the tree.

Since inorder traversal of a BST gives sorted output, the minimum difference
must occur between two consecutive elements in the inorder sequence.

Examples:
    Input: root = [4,2,6,1,3]
    Output: 1
    Explanation: Differences between consecutive inorder values [1,2,3,4,6]:
                 2-1=1, 3-2=1, 4-3=1, 6-4=2. Minimum is 1.

    Input: root = [1,0,48,None,None,12,49]
    Output: 1
    Explanation: Inorder: [0,1,12,48,49]. Min diff = 1-0 = 1.

Constraints:
    - Number of nodes in the tree is in range [2, 10^4]
    - 0 <= Node.val <= 10^5

Hint:
    Do an inorder traversal and track the previous node's value. The minimum
    difference must be between two consecutive nodes in the sorted order.

Pattern: Inorder traversal of BST produces sorted sequence. Compare adjacent
elements to find minimum difference.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_difference(root: TreeNode) -> int:
    """Return the minimum absolute difference between any two nodes in BST."""
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
    # Test 1: Basic BST
    root = build_bst([4, 2, 6, 1, 3])
    assert get_minimum_difference(root) == 1, f"Expected 1, got {get_minimum_difference(root)}"

    # Test 2: BST with larger gaps
    root = build_bst([1, 0, 48, None, None, 12, 49])
    assert get_minimum_difference(root) == 1, f"Expected 1, got {get_minimum_difference(root)}"

    # Test 3: Two nodes
    root = build_bst([1, None, 5])
    assert get_minimum_difference(root) == 4, f"Expected 4, got {get_minimum_difference(root)}"

    # Test 4: Consecutive values
    root = build_bst([2, 1, 3])
    assert get_minimum_difference(root) == 1, f"Expected 1, got {get_minimum_difference(root)}"

    print("All tests passed!")
