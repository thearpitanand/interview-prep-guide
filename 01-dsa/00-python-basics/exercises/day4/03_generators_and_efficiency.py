"""
Exercise: Generators & Efficiency | Day 4
Topic: Generator Expressions and Memory Efficiency

Practice using generators for memory-efficient computation.

Instructions: Implement each function below.
"""


def sum_of_squares_gen(n: int) -> int:
    """Return sum of squares from 1 to n using a generator expression.
    Do NOT use a list comprehension.
    Example: sum_of_squares_gen(3) -> 14  (1 + 4 + 9)
    """
    pass


def any_negative(nums: list[int]) -> bool:
    """Return True if any number is negative, using a generator with any().
    Example: any_negative([1, -2, 3]) -> True
    """
    pass


def all_positive(nums: list[int]) -> bool:
    """Return True if all numbers are positive, using a generator with all().
    Example: all_positive([1, 2, 3]) -> True
    """
    pass


def longest_word_length(words: list[str]) -> int:
    """Return the length of the longest word using a generator with max().
    Return 0 if the list is empty.
    Example: longest_word_length(["hi", "hello", "hey"]) -> 5
    """
    pass


def join_uppercase(words: list[str]) -> str:
    """Join words converted to uppercase with ', ' separator.
    Use a generator with str.join().
    Example: join_uppercase(["hello", "world"]) -> "HELLO, WORLD"
    """
    pass


def count_up_to(n: int):
    """Generator function that yields integers from 1 to n.
    Use the yield keyword.
    Example: list(count_up_to(3)) -> [1, 2, 3]
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert sum_of_squares_gen(3) == 14
    assert sum_of_squares_gen(5) == 55

    assert any_negative([1, -2, 3]) == True
    assert any_negative([1, 2, 3]) == False

    assert all_positive([1, 2, 3]) == True
    assert all_positive([1, -2, 3]) == False

    assert longest_word_length(["hi", "hello", "hey"]) == 5
    assert longest_word_length([]) == 0

    assert join_uppercase(["hello", "world"]) == "HELLO, WORLD"

    assert list(count_up_to(3)) == [1, 2, 3]
    assert list(count_up_to(0)) == []

    print("All tests passed!")
