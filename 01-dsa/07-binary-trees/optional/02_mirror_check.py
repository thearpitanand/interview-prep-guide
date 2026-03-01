"""
Problem: Check if 2 Trees are Mirror (GFG) | Optional | Easy
Topic: Binary Trees

Given two binary trees, check if they are mirrors of each other.

Example 1:
  Input: tree1 =  1       tree2 =  1
                / \\               / \\
               2   3             3   2
  Output: True

Constraints:
  - 0 <= n <= 10^5

Hint: Recursively check: root1.left mirrors root2.right and vice versa.
Pattern: Recursion
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def are_mirrors(root1: TreeNode, root2: TreeNode) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(3), TreeNode(2))
    assert are_mirrors(t1, t2) == True
    assert are_mirrors(t1, t1) == False
    print("All tests passed!")
