"""
Path Sum

Day: 23 | Difficulty: Easy | Pattern: DFS / Path
LeetCode 112: https://leetcode.com/problems/path-sum/

Problem:
    Given the root of a binary tree and an integer targetSum, return true
    if the tree has a root-to-leaf path such that adding up all the values
    along the path equals targetSum.

    A leaf is a node with no children.

Examples:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
    Output: True (path: 5 -> 4 -> 11 -> 2 = 22)

    Input: root = [1,2,3], targetSum = 5
    Output: False

    Input: root = [], targetSum = 0
    Output: False

Constraints:
    - The number of nodes in the tree is in the range [0, 5000].
    - -1000 <= Node.val <= 1000
    - -1000 <= targetSum <= 1000

Hint:
    Subtract the current node's value from targetSum as you go down.
    At a leaf node, check if the remaining sum equals the leaf's value.
    Base case: if node is None, return False.

Pattern: DFS Path (top-down subtraction)
Time: O(n)
Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """Check if there exists a root-to-leaf path with the given sum."""
    pass


# ---------- Tests ----------
if __name__ == "__main__":
    # Test 1: Path 5->4->11->2 = 22
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.right = TreeNode(1)
    assert has_path_sum(root1, 22) is True, "Test 1 failed"

    # Test 2: [1,2,3], target=5 -> False
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert has_path_sum(root2, 5) is False, "Test 2 failed"

    # Test 3: Empty tree, target=0 -> False
    assert has_path_sum(None, 0) is False, "Test 3 failed"

    # Test 4: Single node [1], target=1 -> True
    root4 = TreeNode(1)
    assert has_path_sum(root4, 1) is True, "Test 4 failed"

    # Test 5: Single node [1], target=2 -> False
    assert has_path_sum(root4, 2) is False, "Test 5 failed"

    # Test 6: Negative values [-2,null,-3], target=-5 -> True
    root6 = TreeNode(-2)
    root6.right = TreeNode(-3)
    assert has_path_sum(root6, -5) is True, "Test 6 failed"

    print("All tests passed!")
