"""
Insert into a Binary Search Tree (LC 701)

Day: 26 | Difficulty: Medium | Pattern: BST Insert

You are given the root of a BST and a value to insert into the tree. Return
the root of the BST after the insertion. It is guaranteed that the new value
does not exist in the original BST.

You may return any valid BST after insertion (there may be multiple valid
answers).

Examples:
    Input: root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5] (5 is inserted as left child of 7)

    Input: root = [40,20,60,10,30,50,70], val = 25
    Output: [40,20,60,10,30,50,70,None,None,25] (25 as left child of 30)

Constraints:
    - Number of nodes in the tree is in range [0, 10^4]
    - -10^8 <= Node.val <= 10^8
    - All values in BST are unique
    - val is guaranteed not to exist in the original BST

Hint:
    Traverse the tree using BST property (go left if val < node, right if
    val > node). When you reach a None position, that's where the new node
    goes. Insertion always happens at a leaf position.

Pattern: BST Insert - traverse using BST property, insert at leaf position.
Both recursive and iterative approaches work well.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Insert val into BST and return root. Recursive approach."""
    pass


def insert_into_bst_iterative(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Insert val into BST iteratively."""
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
    """Get inorder traversal of tree."""
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
    # Test 1: Insert into standard BST
    root = build_tree([4, 2, 7, 1, 3])
    result = insert_into_bst(root, 5)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert search(result, 5), "Value 5 not found in tree after insertion"
    assert sorted(inorder(result)) == [1, 2, 3, 4, 5, 7], f"Unexpected inorder: {inorder(result)}"

    # Test 2: Insert into empty tree
    result = insert_into_bst(None, 5)
    assert result.val == 5, f"Expected root value 5, got {result.val}"

    # Test 3: Insert smaller than all
    root = build_tree([4, 2, 7, 1, 3])
    result = insert_into_bst(root, 0)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert search(result, 0), "Value 0 not found in tree after insertion"

    # Test 4: Insert larger than all
    root = build_tree([4, 2, 7, 1, 3])
    result = insert_into_bst(root, 10)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert search(result, 10), "Value 10 not found in tree after insertion"

    # Test 5: Iterative approach
    root = build_tree([40, 20, 60, 10, 30, 50, 70])
    result = insert_into_bst_iterative(root, 25)
    assert is_valid_bst(result), "Iterative: Result is not a valid BST"
    assert search(result, 25), "Iterative: Value 25 not found"

    print("All tests passed!")
