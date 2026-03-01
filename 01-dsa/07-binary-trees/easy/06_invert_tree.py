"""
Invert Binary Tree

Day: 23 | Difficulty: Easy | Pattern: DFS
LeetCode 226: https://leetcode.com/problems/invert-binary-tree/

Problem:
    Given the root of a binary tree, invert the tree (mirror it),
    and return its root.

Examples:
    Input: root = [4,2,7,1,3,6,9]
           4                 4
          / \      ->       / \
         2   7             7   2
        / \ / \           / \ / \
       1  3 6  9         9  6 3  1
    Output: [4,7,2,9,6,3,1]

    Input: root = [2,1,3]
    Output: [2,3,1]

    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 100].
    - -100 <= Node.val <= 100

Hint:
    For each node, swap its left and right children, then recursively
    invert the left and right subtrees. Base case: if node is None, return None.

Pattern: DFS Recursive (swap children)
Time: O(n)
Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    """Invert (mirror) a binary tree and return the root."""
    pass


# ---------- Helper for testing ----------
def tree_to_list(root):
    """Convert tree to level-order list for easy comparison."""
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
    # Test 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root1 = TreeNode(4)
    root1.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root1.right = TreeNode(7, TreeNode(6), TreeNode(9))
    result1 = invert_tree(root1)
    assert tree_to_list(result1) == [4, 7, 2, 9, 6, 3, 1], f"Test 1 failed: {tree_to_list(result1)}"

    # Test 2: [2,1,3] -> [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    result2 = invert_tree(root2)
    assert tree_to_list(result2) == [2, 3, 1], f"Test 2 failed: {tree_to_list(result2)}"

    # Test 3: [] -> []
    assert invert_tree(None) is None, "Test 3 failed"

    # Test 4: [1] -> [1]
    root4 = TreeNode(1)
    result4 = invert_tree(root4)
    assert tree_to_list(result4) == [1], f"Test 4 failed"

    print("All tests passed!")
