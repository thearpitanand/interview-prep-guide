"""
Exercise: TreeNode Class | Day 3
Topic: Python OOP - Building Tree Nodes

Practice building and using tree node classes with OOP patterns.
Focus is on class construction, not tree algorithms.

Instructions: Implement each class/function below.
"""


class TreeNode:
    """A binary tree node.

    Attributes: val, left, right
    - __init__(val=0, left=None, right=None)
    - __str__(): Return str(val)
    - __repr__(): Return "TreeNode(val)"
    - is_leaf(): Return True if node has no children
    """

    def __init__(self, val=0, left=None, right=None):
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def is_leaf(self) -> bool:
        pass


def insert_left(node: TreeNode, val: int) -> TreeNode:
    """Create a new TreeNode with given val and attach as node's left child.
    Return the newly created node.
    Example:
        root = TreeNode(1)
        left = insert_left(root, 2)
        # root.left is now TreeNode(2)
    """
    pass


def insert_right(node: TreeNode, val: int) -> TreeNode:
    """Create a new TreeNode with given val and attach as node's right child.
    Return the newly created node.
    """
    pass


def build_simple_tree() -> TreeNode:
    """Manually build and return this specific tree using TreeNode:

            1
           / \\
          2   3
         / \\
        4   5

    Do NOT use any algorithm. Just create nodes and link them.
    """
    pass


def count_leaves(root: TreeNode) -> int:
    """Count leaf nodes in the tree using the is_leaf() method.
    Return 0 if root is None.

    Hint: A leaf is a node where is_leaf() returns True.
    Use simple recursion: if leaf, return 1; else recurse on children.
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    # TreeNode basic tests
    node = TreeNode(5)
    assert hasattr(node, "val"), "TreeNode must have 'val' attribute"
    assert node.val == 5
    assert node.left is None
    assert node.right is None
    assert node.is_leaf() == True

    node.left = TreeNode(3)
    assert node.is_leaf() == False
    assert str(node) == "5"
    assert repr(node) == "TreeNode(5)"

    # insert_left and insert_right
    root = TreeNode(1)
    left = insert_left(root, 2)
    right = insert_right(root, 3)
    assert root.left.val == 2
    assert root.right.val == 3
    assert left.is_leaf() == True
    assert root.is_leaf() == False

    # build_simple_tree
    tree = build_simple_tree()
    assert tree.val == 1
    assert tree.left.val == 2
    assert tree.right.val == 3
    assert tree.left.left.val == 4
    assert tree.left.right.val == 5
    assert tree.right.is_leaf() == True

    # count_leaves
    assert count_leaves(tree) == 3  # nodes 3, 4, 5 are leaves
    assert count_leaves(None) == 0
    assert count_leaves(TreeNode(1)) == 1

    print("All tests passed!")
