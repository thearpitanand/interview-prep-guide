"""
Exercise: String Basics | Day 1
Topic: Python Basics

Practice string operations, slicing, and methods.

Instructions: Implement each function below.
"""


def first_and_last(s: str) -> str:
    """Return first and last character concatenated.
    Example: first_and_last("hello") -> "ho"
    """
    pass


def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome (case-insensitive).
    Example: is_palindrome("Racecar") -> True
    """
    pass


def count_words(s: str) -> int:
    """Count the number of words in a string.
    Words are separated by spaces.
    """
    pass


def title_case(s: str) -> str:
    """Convert string to title case without using .title().
    Example: title_case("hello world") -> "Hello World"
    """
    pass


def remove_duplicates(s: str) -> str:
    """Remove duplicate characters, keeping first occurrence.
    Example: remove_duplicates("hello") -> "helo"
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert first_and_last("hello") == "ho"
    assert first_and_last("a") == "aa"

    assert is_palindrome("Racecar") == True
    assert is_palindrome("hello") == False

    assert count_words("hello world") == 2
    assert count_words("one") == 1

    assert title_case("hello world") == "Hello World"

    assert remove_duplicates("hello") == "helo"
    assert remove_duplicates("aabbcc") == "abc"
    print("All tests passed!")
