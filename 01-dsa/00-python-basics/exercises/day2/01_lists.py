"""
Exercise: Lists | Day 2
Topic: Python Collections

Practice list operations, slicing, and manipulation.

Instructions: Implement each function below.
"""


def second_largest(nums: list[int]) -> int:
    """Return the second largest number in the list.
    Assume list has at least 2 unique numbers.
    Do NOT use sort.
    """
    pass


def rotate_left(nums: list[int], k: int) -> list[int]:
    """Rotate list left by k positions.
    Example: rotate_left([1,2,3,4,5], 2) -> [3,4,5,1,2]
    """
    pass


def flatten(nested: list) -> list:
    """Flatten a nested list (one level deep).
    Example: flatten([[1,2],[3,4],[5]]) -> [1,2,3,4,5]
    """
    pass


def chunk(lst: list, size: int) -> list[list]:
    """Split list into chunks of given size.
    Example: chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
    """
    pass


def remove_all(lst: list, value) -> list:
    """Remove all occurrences of value from list.
    Return new list, don't modify original.
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert second_largest([3, 1, 4, 1, 5, 9]) == 5
    assert second_largest([1, 2]) == 1

    assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert rotate_left([1, 2, 3], 0) == [1, 2, 3]

    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([1, 2, 3], 3) == [[1, 2, 3]]

    assert remove_all([1, 2, 3, 2, 4], 2) == [1, 3, 4]
    print("All tests passed!")
