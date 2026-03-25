"""
Exercise: Pythonic Rewrites | Day 4
Topic: Rewriting Verbose Code with Comprehensions

Practice converting loop-based code into Pythonic one-liners.

Instructions: Implement each function using comprehensions or generators.
"""


def get_even_squares(nums: list[int]) -> list[int]:
    """Given a list of numbers, return squares of even numbers only.

    Verbose version:
        result = []
        for n in nums:
            if n % 2 == 0:
                result.append(n ** 2)
        return result

    Rewrite using a list comprehension.
    """
    pass


def invert_dict(d: dict) -> dict:
    """Swap keys and values using a dict comprehension.

    Verbose version:
        result = {}
        for k, v in d.items():
            result[v] = k
        return result
    """
    pass


def extract_unique_chars(s: str) -> set:
    """Return set of lowercase letters in the string using a set comprehension.
    Only include alphabetic characters.

    Verbose version:
        result = set()
        for ch in s:
            if ch.isalpha():
                result.add(ch.lower())
        return result
    """
    pass


def sum_of_multiples(n: int, k: int) -> int:
    """Return sum of all multiples of k less than n, using a generator.

    Verbose version:
        total = 0
        for i in range(1, n):
            if i % k == 0:
                total += i
        return total
    """
    pass


def matrix_to_flat_sorted(matrix: list[list[int]]) -> list[int]:
    """Flatten a 2D matrix and return sorted values using a comprehension.

    Verbose version:
        result = []
        for row in matrix:
            for val in row:
                result.append(val)
        result.sort()
        return result
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert get_even_squares([1, 2, 3, 4, 5]) == [4, 16]

    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    assert extract_unique_chars("Hello, World!") == {"h", "e", "l", "o", "w", "r", "d"}

    assert sum_of_multiples(10, 3) == 18  # 3 + 6 + 9

    assert matrix_to_flat_sorted([[3, 1], [4, 2]]) == [1, 2, 3, 4]

    print("All tests passed!")
