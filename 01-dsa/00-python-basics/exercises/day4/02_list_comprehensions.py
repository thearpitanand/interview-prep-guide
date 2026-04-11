"""
Exercise: List Comprehensions | Day 4
Topic: Python Comprehensions

Practice list, dict, and set comprehensions.

Instructions: Implement each function using comprehensions.
"""

from collections import defaultdict


def squares(n: int) -> list[int]:
    """Return list of squares from 1 to n using list comprehension.
    Example: squares(5) -> [1, 4, 9, 16, 25]
    """
    return [x**2 for x in range(1, n + 1)]


def even_filter(nums: list[int]) -> list[int]:
    """Return only even numbers using list comprehension."""
    return [x for x in nums if x % 2 == 0]


def flatten_2d(matrix: list[list[int]]) -> list[int]:
    """Flatten a 2D list using list comprehension.
    Example: flatten_2d([[1,2],[3,4]]) -> [1,2,3,4]
    """
    return [x for row in matrix for x in row]


def char_frequency(s: str) -> dict[str, int]:
    """Return character frequency dict using dict comprehension.
    Only include characters that appear more than once.
    """
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1

    # return freq
    return {k: v for k, v in freq.items() if v >= 2}


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a matrix using list comprehension.
    Example: transpose([[1,2],[3,4]]) -> [[1,3],[2,4]]
    """
    transposed_matrix = []

    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed_matrix.append(row)

    return transposed_matrix
    # return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# --- Tests ---
if __name__ == "__main__":
    assert squares(5) == [1, 4, 9, 16, 25]

    assert even_filter([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    assert flatten_2d([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    freq = char_frequency("hello")
    assert freq == {"l": 2}

    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    print("All tests passed!")
