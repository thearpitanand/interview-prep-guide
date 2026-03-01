"""
Serialize and Deserialize Binary Tree

Day: 25 | Difficulty: Hard | Pattern: BFS / DFS
LeetCode 297: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Problem:
    Design an algorithm to serialize and deserialize a binary tree. There is
    no restriction on how your serialization/deserialization algorithm should
    work. You just need to ensure that a binary tree can be serialized to a
    string and this string can be deserialized to the original tree structure.

Examples:
    Input: root = [1,2,3,null,null,4,5]
           1
          / \
         2   3
            / \
           4   5
    Output: [1,2,3,null,null,4,5]  (serialize then deserialize should
            reproduce the same tree)

    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 10^4].
    - -1000 <= Node.val <= 1000

Hint:
    BFS approach: Use level-order traversal with "null" for missing nodes.
    Serialize: BFS, append values or "null" to a list, join with commas.
    Deserialize: Split the string, use a queue to rebuild level by level.

    DFS approach: Use preorder traversal with a sentinel for null nodes.
    Serialize: preorder with "null" markers.
    Deserialize: use an iterator to rebuild recursively.

Pattern: BFS or DFS with null markers
Time: O(n) for both serialize and deserialize
Space: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """Serialize and deserialize a binary tree."""

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        pass

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        pass


# ---------- Helper for testing ----------
def trees_equal(t1, t2):
    """Check if two trees are structurally identical with same values."""
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val and
            trees_equal(t1.left, t2.left) and
            trees_equal(t1.right, t2.right))


# ---------- Tests ----------
if __name__ == "__main__":
    codec = Codec()

    # Test 1: [1,2,3,null,null,4,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3, TreeNode(4), TreeNode(5))
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    assert trees_equal(root1, deserialized1), f"Test 1 failed. Serialized: {serialized1}"

    # Test 2: Empty tree
    serialized2 = codec.serialize(None)
    deserialized2 = codec.deserialize(serialized2)
    assert deserialized2 is None, "Test 2 failed"

    # Test 3: Single node
    root3 = TreeNode(42)
    serialized3 = codec.serialize(root3)
    deserialized3 = codec.deserialize(serialized3)
    assert trees_equal(root3, deserialized3), "Test 3 failed"

    # Test 4: Left-skewed tree
    root4 = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    serialized4 = codec.serialize(root4)
    deserialized4 = codec.deserialize(serialized4)
    assert trees_equal(root4, deserialized4), "Test 4 failed"

    # Test 5: Negative values
    root5 = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    serialized5 = codec.serialize(root5)
    deserialized5 = codec.deserialize(serialized5)
    assert trees_equal(root5, deserialized5), "Test 5 failed"

    # Test 6: Roundtrip idempotent
    assert codec.serialize(codec.deserialize(serialized1)) == serialized1, "Test 6 failed"

    print("All tests passed!")
