"""
Exercise: List Comprehensions | Day 3
Topic: Python Comprehensions

Practice list, dict, and set comprehensions.

Instructions: Implement each function using comprehensions.
"""


def squares(n: int) -> list[int]:
    """Return list of squares from 1 to n using list comprehension.
    Example: squares(5) -> [1, 4, 9, 16, 25]
    """
    pass


def even_filter(nums: list[int]) -> list[int]:
    """Return only even numbers using list comprehension."""
    pass


def flatten_2d(matrix: list[list[int]]) -> list[int]:
    """Flatten a 2D list using list comprehension.
    Example: flatten_2d([[1,2],[3,4]]) -> [1,2,3,4]
    """
    pass


def char_frequency(s: str) -> dict[str, int]:
    """Return character frequency dict using dict comprehension.
    Only include characters that appear more than once.
    """
    pass


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a matrix using list comprehension.
    Example: transpose([[1,2],[3,4]]) -> [[1,3],[2,4]]
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert squares(5) == [1, 4, 9, 16, 25]

    assert even_filter([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    assert flatten_2d([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    freq = char_frequency("hello")
    assert freq == {'l': 2}

    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    print("All tests passed!")
