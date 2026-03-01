"""
Convert Sorted Array to Binary Search Tree (LC 108)

Day: 26 | Difficulty: Easy | Pattern: Divide and Conquer

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced BST.

A height-balanced BST is a BST in which the depth of the two subtrees of every
node never differs by more than one.

Examples:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,None,5] (one possible valid answer)
    Explanation: Pick middle element (0) as root, recursively build left and
                 right subtrees from left and right halves.

    Input: nums = [1,3]
    Output: [3,1] or [1,None,3] (either is valid)

Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums is sorted in strictly increasing order

Hint:
    Always pick the middle element as the root to ensure balance. Recursively
    apply the same strategy to left half (left subtree) and right half (right
    subtree).

Pattern: Divide and Conquer - pick middle element as root, recursively build
left subtree from left half and right subtree from right half.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    """Convert a sorted array to a height-balanced BST."""
    pass


# --- Helper Functions ---

def tree_to_list(root):
    """Convert tree to level-order list for verification."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    """Check if tree is a valid BST."""
    if not root:
        return True
    if root.val <= low or root.val >= high:
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)


def get_height(root):
    """Get height of tree."""
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def is_balanced(root):
    """Check if tree is height-balanced."""
    if not root:
        return True
    left_h = get_height(root.left)
    right_h = get_height(root.right)
    if abs(left_h - right_h) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


def inorder(root):
    """Get inorder traversal."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard sorted array
    nums = [-10, -3, 0, 5, 9]
    result = sorted_array_to_bst(nums)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert is_balanced(result), "Result is not height-balanced"
    assert inorder(result) == nums, f"Inorder traversal doesn't match input: {inorder(result)}"

    # Test 2: Two elements
    nums = [1, 3]
    result = sorted_array_to_bst(nums)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert is_balanced(result), "Result is not height-balanced"
    assert inorder(result) == nums, f"Inorder traversal doesn't match input"

    # Test 3: Single element
    nums = [0]
    result = sorted_array_to_bst(nums)
    assert result.val == 0, f"Expected root value 0, got {result.val}"
    assert result.left is None and result.right is None

    # Test 4: Larger array
    nums = [1, 2, 3, 4, 5, 6, 7]
    result = sorted_array_to_bst(nums)
    assert is_valid_bst(result), "Result is not a valid BST"
    assert is_balanced(result), "Result is not height-balanced"
    assert inorder(result) == nums, f"Inorder traversal doesn't match input"

    print("All tests passed!")
