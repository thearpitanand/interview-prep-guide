"""
Binary Tree Inorder Traversal

Day: 23 | Difficulty: Easy | Pattern: DFS
LeetCode 94: https://leetcode.com/problems/binary-tree-inorder-traversal/

Problem:
    Given the root of a binary tree, return the inorder traversal of its
    nodes' values. Inorder means: Left -> Root -> Right.

Examples:
    Input: root = [1, null, 2, 3]
         1
          \
           2
          /
         3
    Output: [1, 3, 2]

    Input: root = []
    Output: []

    Input: root = [1]
    Output: [1]

Constraints:
    - The number of nodes in the tree is in the range [0, 100].
    - -100 <= Node.val <= 100

Hint:
    Recursive: base case is empty node. Recurse left, add root, recurse right.
    Iterative: use a stack. Go as far left as possible, then process and go right.

Pattern: DFS Recursive / Iterative with Stack
Time: O(n) - visit every node
Space: O(h) - recursion stack / explicit stack, h = height
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> list[int]:
    """Return inorder traversal of binary tree."""
    pass


def inorder_traversal_iterative(root: TreeNode) -> list[int]:
    """Return inorder traversal using iterative approach with stack."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1, null, 2, 3] -> [1, 3, 2]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert inorder_traversal(root1) == [1, 3, 2], f"Test 1 failed: {inorder_traversal(root1)}"

    # Test 2: [] -> []
    assert inorder_traversal(None) == [], f"Test 2 failed: {inorder_traversal(None)}"

    # Test 3: [1] -> [1]
    root3 = TreeNode(1)
    assert inorder_traversal(root3) == [1], f"Test 3 failed: {inorder_traversal(root3)}"

    # Test 4: Full tree [1,2,3,4,5] -> [4,2,5,1,3]
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    assert inorder_traversal(root4) == [4, 2, 5, 1, 3], f"Test 4 failed"

    # Test iterative version
    assert inorder_traversal_iterative(root1) == [1, 3, 2], "Iterative Test 1 failed"
    assert inorder_traversal_iterative(None) == [], "Iterative Test 2 failed"
    assert inorder_traversal_iterative(root4) == [4, 2, 5, 1, 3], "Iterative Test 4 failed"

    print("All tests passed!")
