"""
Problem: Distance Between 2 Nodes (GFG) | Optional | Medium
Topic: Binary Trees

Find the distance (number of edges) between two nodes in a binary tree.

Example 1:
  Input: root = [1,2,3], node1 = 2, node2 = 3
  Output: 2

Constraints:
  - 1 <= n <= 10^4

Hint: dist(a,b) = dist(root,a) + dist(root,b) - 2*dist(root,LCA(a,b)).
Pattern: LCA + Distance
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distance_between_nodes(root: TreeNode, a: int, b: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert distance_between_nodes(root, 2, 3) == 2
    assert distance_between_nodes(root, 1, 3) == 1
    print("All tests passed!")
