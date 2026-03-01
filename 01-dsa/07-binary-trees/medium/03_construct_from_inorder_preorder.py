"""
Construct Binary Tree from Preorder and Inorder Traversal

Day: 24 | Difficulty: Medium | Pattern: DFS
LeetCode 105: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem:
    Given two integer arrays preorder and inorder where preorder is the
    preorder traversal of a binary tree and inorder is the inorder traversal
    of the same tree, construct and return the binary tree.

Examples:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output:
         3
        / \
       9   20
          /  \
         15   7

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    - 1 <= preorder.length <= 3000
    - inorder.length == preorder.length
    - -3000 <= preorder[i], inorder[i] <= 3000
    - preorder and inorder consist of unique values.
    - Each value of inorder also appears in preorder.
    - preorder is guaranteed to be the preorder traversal of the tree.
    - inorder is guaranteed to be the inorder traversal of the tree.

Hint:
    - First element of preorder is always the root.
    - Find that element in inorder -> everything to the left is left subtree,
      everything to the right is right subtree.
    - Use a hashmap for O(1) lookup in inorder.
    - Recursively build left and right subtrees.

Pattern: DFS + HashMap for index lookup
Time: O(n)
Space: O(n) - hashmap + recursion stack
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    """Construct binary tree from preorder and inorder traversals."""
    pass


# ---------- Helper for testing ----------
def tree_to_list(root):
    """Convert tree to level-order list."""
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
    root1 = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_to_list(root1) == [3, 9, 20, None, None, 15, 7], (
        f"Test 1 failed: {tree_to_list(root1)}"
    )

    # Test 2: preorder=[-1], inorder=[-1]
    root2 = build_tree([-1], [-1])
    assert tree_to_list(root2) == [-1], f"Test 2 failed: {tree_to_list(root2)}"

    # Test 3: preorder=[1,2], inorder=[2,1]
    root3 = build_tree([1, 2], [2, 1])
    assert root3.val == 1, "Test 3 failed: root should be 1"
    assert root3.left.val == 2, "Test 3 failed: left child should be 2"
    assert root3.right is None, "Test 3 failed: right child should be None"

    # Test 4: preorder=[1,2,3], inorder=[2,1,3]
    root4 = build_tree([1, 2, 3], [2, 1, 3])
    assert tree_to_list(root4) == [1, 2, 3], f"Test 4 failed: {tree_to_list(root4)}"

    print("All tests passed!")
