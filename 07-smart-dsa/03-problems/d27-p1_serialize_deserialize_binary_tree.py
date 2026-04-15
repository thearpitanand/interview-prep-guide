"""
Problem: Serialize and Deserialize Binary Tree (LC 297) | Smart-DSA Day 27 | Hard
Pattern: Tree DFS
Time target: 40 minutes

Design an algorithm to serialize a binary tree to a string and deserialize
that string back to the original tree structure. There is no restriction on
the format of the serialized string.

Example 1:
  Input: root = [1,2,3,null,null,4,5]
  Output: [1,2,3,null,null,4,5]  (tree is reconstructed identically)

Example 2:
  Input: root = []
  Output: []

Constraints:
  - The number of nodes is in [0, 10^4].
  - -1000 <= Node.val <= 1000

Hint (⚠ read only after time budget is blown):
  Pre-order DFS: serialize by appending node.val (or "N" for null) to a list
  joined by commas. Deserialize by consuming values from an iterator in the
  same pre-order: if value is "N" return None, else create a node and
  recursively build left then right subtrees.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: TreeNode | None) -> str:
    pass


def deserialize(data: str) -> TreeNode | None:
    pass


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


if __name__ == "__main__":
    # [1,2,3,null,null,4,5]
    root1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data1 = serialize(root1)
    reconstructed1 = deserialize(data1)
    assert _level_order(reconstructed1) == _level_order(root1)

    # Empty tree
    data2 = serialize(None)
    assert deserialize(data2) is None

    # Single node
    root3 = TreeNode(42)
    data3 = serialize(root3)
    reconstructed3 = deserialize(data3)
    assert reconstructed3 is not None and reconstructed3.val == 42

    # Left-skewed [1,2,3]
    root4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    data4 = serialize(root4)
    reconstructed4 = deserialize(data4)
    assert _level_order(reconstructed4) == _level_order(root4)

    print("All tests passed!")
