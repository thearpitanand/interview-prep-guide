"""
Binary Search Tree Iterator (LC 173)

Day: 27 | Difficulty: Medium | Pattern: Controlled Inorder Traversal

Implement the BSTIterator class that represents an iterator over the inorder
traversal of a BST:

- BSTIterator(TreeNode root): Initializes the iterator. The pointer is
  initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext(): Returns True if there exists a number in the traversal
  to the right of the pointer.
- int next(): Moves the pointer to the right, then returns the number at
  the pointer.

next() and hasNext() should run in average O(1) time and use O(h) memory,
where h is the height of the tree.

Examples:
    Input: BST = [7,3,15,None,None,9,20]
    Operations: next(), next(), hasNext(), next(), hasNext(), next(), hasNext(), next(), hasNext()
    Output:     [3,     7,     True,     9,     True,      15,    True,      20,    False]

Constraints:
    - Number of nodes in the tree is in range [1, 10^5]
    - 0 <= Node.val <= 10^6
    - At most 10^5 calls to hasNext and next
    - All calls to next are valid (there is at least one next element)

Hint:
    Use a stack to simulate the inorder traversal. Initially push all left
    nodes onto the stack. For next(), pop from stack, and if the popped node
    has a right child, push all left children of the right child.

    This is called "controlled recursion" - you control when to advance the
    inorder traversal step by step.

Pattern: Controlled Inorder - use explicit stack to pause/resume inorder
traversal on demand. Push all left children, pop for next value, then
handle right subtree.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """Iterator for BST inorder traversal using controlled recursion with stack."""

    def __init__(self, root: Optional[TreeNode]):
        """Initialize iterator with root of BST."""
        pass

    def next(self) -> int:
        """Return the next smallest number in BST."""
        pass

    def has_next(self) -> bool:
        """Return whether we have a next smallest number."""
        pass


# --- Helper Functions ---

def build_tree(values):
    """Build a binary tree from a level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard iteration
    root = build_tree([7, 3, 15, None, None, 9, 20])
    iterator = BSTIterator(root)

    assert iterator.next() == 3, "Expected 3"
    assert iterator.next() == 7, "Expected 7"
    assert iterator.has_next() == True, "Expected True"
    assert iterator.next() == 9, "Expected 9"
    assert iterator.has_next() == True, "Expected True"
    assert iterator.next() == 15, "Expected 15"
    assert iterator.has_next() == True, "Expected True"
    assert iterator.next() == 20, "Expected 20"
    assert iterator.has_next() == False, "Expected False"

    # Test 2: Single node
    root = build_tree([1])
    iterator = BSTIterator(root)
    assert iterator.has_next() == True, "Expected True"
    assert iterator.next() == 1, "Expected 1"
    assert iterator.has_next() == False, "Expected False"

    # Test 3: Left-skewed tree
    root = build_tree([3, 2, None, 1])
    iterator = BSTIterator(root)
    assert iterator.next() == 1, "Expected 1"
    assert iterator.next() == 2, "Expected 2"
    assert iterator.next() == 3, "Expected 3"
    assert iterator.has_next() == False, "Expected False"

    # Test 4: Right-skewed tree
    root = build_tree([1, None, 2, None, 3])
    iterator = BSTIterator(root)
    assert iterator.next() == 1, "Expected 1"
    assert iterator.next() == 2, "Expected 2"
    assert iterator.next() == 3, "Expected 3"
    assert iterator.has_next() == False, "Expected False"

    # Test 5: Collect all values
    root = build_tree([5, 3, 7, 2, 4, 6, 8])
    iterator = BSTIterator(root)
    values = []
    while iterator.has_next():
        values.append(iterator.next())
    assert values == [2, 3, 4, 5, 6, 7, 8], f"Expected [2,3,4,5,6,7,8], got {values}"

    print("All tests passed!")
