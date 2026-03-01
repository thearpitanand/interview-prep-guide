"""
Flatten Binary Tree to Linked List

Day: 24 | Difficulty: Medium | Pattern: DFS
LeetCode 114: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Problem:
    Given the root of a binary tree, flatten the tree into a "linked list":
    - The "linked list" should use the same TreeNode class where the right
      child pointer points to the next node and the left child pointer is
      always null.
    - The "linked list" should be in the same order as a preorder traversal.

Examples:
    Input: root = [1,2,5,3,4,null,6]
           1
          / \
         2   5
        / \   \
       3   4   6

    Output: [1,null,2,null,3,null,4,null,5,null,6]
       1
        \
         2
          \
           3
            \
             4
              \
               5
                \
                 6

    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 2000].
    - -100 <= Node.val <= 100

Hint:
    Approach 1 (Reverse Postorder): Process right, left, root. Keep a 'prev'
    pointer. Set node.right = prev, node.left = None, then prev = node.

    Approach 2 (Morris-like): For each node, find the rightmost node in the
    left subtree, connect it to node.right, then move node.left to node.right.

Pattern: DFS (reverse postorder or iterative)
Time: O(n)
Space: O(h) for recursive, O(1) for Morris-like
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode) -> None:
    """Flatten binary tree to linked list in-place. Modifies the tree."""
    pass


# ---------- Helper for testing ----------
def linked_list_to_list(root):
    """Convert right-linked list to a Python list."""
    result = []
    while root:
        assert root.left is None, f"Node {root.val} has non-null left child"
        result.append(root.val)
        root = root.right
    return result


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,2,5,3,4,null,6] -> [1,2,3,4,5,6]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(5, None, TreeNode(6))
    flatten(root1)
    assert linked_list_to_list(root1) == [1, 2, 3, 4, 5, 6], (
        f"Test 1 failed: {linked_list_to_list(root1)}"
    )

    # Test 2: [] -> []
    flatten(None)  # Should not crash

    # Test 3: [0] -> [0]
    root3 = TreeNode(0)
    flatten(root3)
    assert linked_list_to_list(root3) == [0], "Test 3 failed"

    # Test 4: [1,2] -> [1,2]
    root4 = TreeNode(1, TreeNode(2))
    flatten(root4)
    assert linked_list_to_list(root4) == [1, 2], f"Test 4 failed: {linked_list_to_list(root4)}"

    # Test 5: [1,null,2] -> [1,2]
    root5 = TreeNode(1, None, TreeNode(2))
    flatten(root5)
    assert linked_list_to_list(root5) == [1, 2], f"Test 5 failed: {linked_list_to_list(root5)}"

    print("All tests passed!")
