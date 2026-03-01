"""
Same Tree

Day: 23 | Difficulty: Easy | Pattern: DFS
LeetCode 100: https://leetcode.com/problems/same-tree/

Problem:
    Given the roots of two binary trees p and q, write a function to check
    if they are the same or not. Two binary trees are considered the same
    if they are structurally identical and the nodes have the same value.

Examples:
    Input: p = [1,2,3], q = [1,2,3]
    Output: True

    Input: p = [1,2], q = [1,null,2]
    Output: False

    Input: p = [1,2,1], q = [1,1,2]
    Output: False

Constraints:
    - The number of nodes in both trees is in the range [0, 100].
    - -10^4 <= Node.val <= 10^4

Hint:
    Two trees are the same if:
    1. Both are None (base case -> True)
    2. One is None and the other isn't (-> False)
    3. Values are equal AND left subtrees are same AND right subtrees are same

Pattern: DFS Recursive (simultaneous traversal)
Time: O(n) - visit every node in both trees
Space: O(h) - recursion stack
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """Check if two binary trees are identical."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: [1,2,3] and [1,2,3] -> True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p1, q1) is True, "Test 1 failed"

    # Test 2: [1,2] and [1,null,2] -> False
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p2, q2) is False, "Test 2 failed"

    # Test 3: [1,2,1] and [1,1,2] -> False
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(p3, q3) is False, "Test 3 failed"

    # Test 4: Both empty -> True
    assert is_same_tree(None, None) is True, "Test 4 failed"

    # Test 5: One empty, one not -> False
    assert is_same_tree(TreeNode(1), None) is False, "Test 5 failed"

    print("All tests passed!")
