"""
Exercise: Magic Methods | Day 3
Topic: Python Dunder Methods

Practice implementing magic methods for custom classes.

Instructions: Implement each class below.
"""


class Point:
    """A 2D point that supports equality and comparison.

    Methods:
    - __init__(x, y): Store x and y coordinates
    - __eq__(other): Two points are equal if x and y match
    - __lt__(other): Compare by x first, then y (for sorting)
    - __str__(): Return "Point(x, y)"
    - __repr__(): Return "Point(x, y)"
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other) -> bool:
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x})"


class SortableStudent:
    """A student that can be sorted by GPA (descending), then name (ascending).

    This is a common pattern for heapq and sorted().

    Methods:
    - __init__(name, gpa): Store name and gpa
    - __lt__(other): Higher GPA comes first; if tied, alphabetical by name
    - __str__(): Return "name (gpa)"
    - __repr__(): Return "SortableStudent(name, gpa)"
    """

    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other) -> bool:
        if self.gpa != other.gpa:
            return self.gpa > other.gpa
        return self.name < other.name

    def __str__(self) -> str:
        return f"{self.name} ({self.gpa})"

    def __repr__(self) -> str:
        return f"SortableStudent({self.name}, {self.gpa})"


class Matrix:
    """A matrix that supports len() and indexing.

    Methods:
    - __init__(data): Store 2D list
    - __len__(): Return number of rows
    - __getitem__(index): Return row at index (supports m[i])
    - __str__(): Return rows separated by newlines, e.g. "1 2 3\n4 5 6"
    """

    def __init__(self, data: list[list[int]]):
        self.data = data

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index) -> list[int]:
        return self.data[index]

    def __str__(self) -> str:
        rows = []

        for row in self.data:
            result = ""
            for index, item in enumerate(row):
                result += f"{str(item)}{" " if index != len(row) - 1 else ""}"
            rows.append(result)

        return "\n".join(rows)


# --- Tests ---
if __name__ == "__main__":
    # Point tests
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 1)
    assert p1 == p2
    assert not (p1 == p3)
    assert p1 < p3
    assert str(p1) == "Point(1, 2)"

    # Sorting points
    points = [Point(3, 1), Point(1, 5), Point(1, 2)]
    points.sort()
    assert points == [Point(1, 2), Point(1, 5), Point(3, 1)]

    # SortableStudent tests
    s1 = SortableStudent("Alice", 3.8)
    s2 = SortableStudent("Bob", 3.9)
    s3 = SortableStudent("Charlie", 3.8)
    students = [s1, s2, s3]
    students.sort()
    assert students[0].name == "Bob"  # highest GPA first
    assert students[1].name == "Alice"  # same GPA, alphabetical
    assert students[2].name == "Charlie"
    assert str(s1) == "Alice (3.8)"

    # Matrix tests
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    assert len(m) == 2
    assert m[0] == [1, 2, 3]
    assert m[1] == [4, 5, 6]
    assert str(m) == "1 2 3\n4 5 6"

    print("All tests passed!")
