"""
Search in a Binary Search Tree (LC 700)

Day: 26 | Difficulty: Easy | Pattern: BST Search

Given the root of a BST and an integer val, find the node in the BST whose
value equals val. Return the subtree rooted at that node. If no such node
exists, return None.

Examples:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3] (subtree rooted at node with value 2)

    Input: root = [4,2,7,1,3], val = 5
    Output: None

Constraints:
    - Number of nodes in the tree is in range [1, 5000]
    - 1 <= Node.val <= 10^7
    - root is a valid BST
    - 1 <= val <= 10^7

Hint:
    Use the BST property: if val < current node, go left; if val > current
    node, go right. This narrows the search by half at each step.

Pattern: BST Search - compare target with current node and recurse/iterate
in the appropriate direction.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root: TreeNode, val: int) -> TreeNode:
    """Search for a node with given value in BST. Return the subtree rooted at that node."""
    pass


def search_bst_iterative(root: TreeNode, val: int) -> TreeNode:
    """Iterative approach - O(1) space."""
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


def tree_to_list(root):
    """Convert tree to level-order list for easy comparison."""
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
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Value exists in tree
    root = build_bst([4, 2, 7, 1, 3])
    result = search_bst(root, 2)
    assert tree_to_list(result) == [2, 1, 3], f"Expected [2, 1, 3], got {tree_to_list(result)}"

    # Test 2: Value does not exist
    root = build_bst([4, 2, 7, 1, 3])
    result = search_bst(root, 5)
    assert result is None, f"Expected None, got {result}"

    # Test 3: Value is root
    root = build_bst([4, 2, 7, 1, 3])
    result = search_bst(root, 4)
    assert tree_to_list(result) == [4, 2, 7, 1, 3], f"Expected [4, 2, 7, 1, 3], got {tree_to_list(result)}"

    # Test 4: Iterative approach
    root = build_bst([4, 2, 7, 1, 3])
    result = search_bst_iterative(root, 2)
    assert tree_to_list(result) == [2, 1, 3], f"Expected [2, 1, 3], got {tree_to_list(result)}"

    # Test 5: Single node tree
    root = build_bst([1])
    result = search_bst(root, 1)
    assert tree_to_list(result) == [1], f"Expected [1], got {tree_to_list(result)}"

    print("All tests passed!")
