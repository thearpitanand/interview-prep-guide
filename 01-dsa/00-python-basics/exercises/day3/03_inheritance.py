"""
Exercise: Inheritance | Day 3
Topic: Python Inheritance

Practice inheritance, super(), and method overriding.

Instructions: Implement each class below.
"""

import math


class Shape:
    """Base class for shapes.

    Methods:
    - __init__(name): Store the shape name
    - area(): Return 0 (to be overridden)
    - perimeter(): Return 0 (to be overridden)
    - __str__(): Return "name: area=X.XX" (2 decimal places)
    """

    def __init__(self, name: str):
        self.name = name

    def area(self) -> float:
        return 0

    def perimeter(self) -> float:
        return 0

    def __str__(self) -> str:
        return f"{self.name}: {round(self.area(), 2)}"


class Rectangle(Shape):
    """A rectangle. Inherits from Shape.

    - __init__(width, height): Call super().__init__("Rectangle"), store dimensions
    - area(): Return width * height
    - perimeter(): Return 2 * (width + height)
    """

    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """A circle. Inherits from Shape.

    - __init__(radius): Call super().__init__("Circle"), store radius
    - area(): Return pi * r^2
    - perimeter(): Return 2 * pi * r
    """

    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class ListNode:
    """A node in a singly linked list (base class).

    - __init__(val=0, next=None): Store val and next
    - __str__():Return "val -> next_val -> ... -> None"
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = []
        curr = self
        while curr != None:
            result.append(str(curr.val))
            curr = curr.next

        return " -> ".join(result) + " -> None"


class DoublyLinkedNode(ListNode):
    """Extends ListNode with a prev pointer using inheritance.

    - __init__(val=0, next=None, prev=None): Call super().__init__(val, next), store prev
    - __str__(): Return "None <-> val <-> next_val <-> ... <-> None"
    """

    def __init__(self, val=0, next=None, prev=None):
        super().__init__(val, next)
        self.prev = prev

    def __str__(self) -> str:
        result = []
        curr = self
        while curr != None:
            result.append(str(curr.val))
            curr = curr.next

        return "None <->" + " <-> ".join(result) + "<-> None"


class TreeNode:
    """A binary tree node (base class).

    - __init__(val=0, left=None, right=None)
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AnnotatedTreeNode(TreeNode):
    """Extends TreeNode with depth and parent tracking.

    - __init__(val=0, left=None, right=None, depth=0, parent=None):
      Call super().__init__(val, left, right), store depth and parent
    - __repr__(): Return "AnnotatedTreeNode(val=X, depth=Y)"
    """

    def __init__(self, val=0, left=None, right=None, depth=0, parent=None):
        super().__init__(val, left, right)
        self.depth = depth
        self.parent = parent

    def __repr__(self) -> str:
        return f"AnnotatedTreeNode(val={self.val}, depth={self.depth})"


# --- Tests ---
if __name__ == "__main__":
    # Shape hierarchy
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14
    assert r.name == "Rectangle"

    c = Circle(5)
    assert abs(c.area() - 78.5398) < 0.01
    assert abs(c.perimeter() - 31.4159) < 0.01
    assert c.name == "Circle"

    # DoublyLinkedNode inherits from ListNode
    n1 = ListNode(1, ListNode(2, ListNode(3)))
    assert str(n1) == "1 -> 2 -> 3 -> None"

    d1 = DoublyLinkedNode(10)
    d2 = DoublyLinkedNode(20, prev=d1)
    d1.next = d2
    assert d1.val == 10  # inherited from ListNode
    assert d1.next.val == 20  # inherited from ListNode
    assert d2.prev.val == 10  # new attribute from DoublyLinkedNode
    assert isinstance(d1, ListNode)  # confirms inheritance

    # AnnotatedTreeNode inherits from TreeNode
    root = AnnotatedTreeNode(val=1, depth=0)
    child = AnnotatedTreeNode(val=2, depth=1, parent=root)
    root.left = child
    assert root.val == 1  # inherited from TreeNode
    assert root.left.val == 2  # inherited from TreeNode
    assert child.depth == 1  # new attribute
    assert child.parent.val == 1  # new attribute
    assert isinstance(root, TreeNode)  # confirms inheritance
    assert repr(child) == "AnnotatedTreeNode(val=2, depth=1)"

    print("All tests passed!")
