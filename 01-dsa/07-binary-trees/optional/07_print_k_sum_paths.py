"""
Problem: Print All K-Sum Paths (GFG) | Optional | Medium
Topic: Binary Trees

Given a binary tree and an integer k, print all paths that sum to k.
Paths can start from any node and end at any node downward.

Example 1:
  Input: root = [1,3,null,2,1,null,1], k = 5
  Output: paths summing to 5

Constraints:
  - 1 <= n <= 10^5

Hint: DFS with path tracking. At each node, check all sub-paths ending here.
Pattern: DFS + Path Tracking
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def k_sum_paths(root: TreeNode, k: int) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(3, TreeNode(2), TreeNode(1, None, TreeNode(1))), None)
    result = k_sum_paths(root, 5)
    assert len(result) >= 1
    print("All tests passed!")
