"""
Problem: Invert Binary Tree (LC 226) | Smart-DSA Day 22 | Easy
Pattern: Tree DFS
Time target: 15 minutes

Given the root of a binary tree, invert the tree (mirror it) and return
its root.

Example 1:
  Input:  root = [4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]

Example 2:
  Input:  root = [2,1,3]
  Output: [2,3,1]

Example 3:
  Input: root = []
  Output: []

Constraints:
  - The number of nodes is in [0, 100].
  - -100 <= Node.val <= 100

Hint (⚠ read only after time budget is blown):
  Recursively invert left and right subtrees, then swap root.left and
  root.right. Base case: None node returns None.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def _level_order(root: TreeNode | None) -> list[int | None]:
    """BFS serialization for comparison."""
    if not root:
        return []
    from collections import deque
    result: list[int | None] = []
    q: deque[TreeNode | None] = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    pass


if __name__ == "__main__":
    # [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root1 = TreeNode(4,
                     TreeNode(2, TreeNode(1), TreeNode(3)),
                     TreeNode(7, TreeNode(6), TreeNode(9)))
    assert _level_order(invert_tree(root1)) == [4, 7, 2, 9, 6, 3, 1]

    # [2,1,3] -> [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert _level_order(invert_tree(root2)) == [2, 3, 1]

    # Empty tree
    assert invert_tree(None) is None

    print("All tests passed!")
