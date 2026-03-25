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

    if len(s) == 0:
        return ""

    if len(s) == 1:
        return s[0] + s[0]

    return s[0] + s[-1]


def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome (case-insensitive).
    Example: is_palindrome("Racecar") -> True
    """
    # "Racecar"
    # 7/2 = 3
    half_len = int(len(s) / 2)
    is_palindrome = True

    # [0, 1, 2]
    # [6, 5, 4]
    for i, j in zip(range(0, half_len), range(len(s) - 1, half_len, -1)):
        if s[i].lower() != s[j].lower():
            is_palindrome = False
            break

    return is_palindrome


def count_words(s: str) -> int:
    """Count the number of words in a string.
    Words are separated by spaces.
    """
    return len(s.split())


def title_case(s: str) -> str:
    """Convert string to title case without using .title().
    Example: title_case("hello world") -> "Hello World"
    """
    result = []
    for n in s.split():
        new_word = n[0].upper() + n[1:].lower()

        # for i in range(1, len(n)):
        #     new_word += n[i]

        result.append(new_word)

    return " ".join(result)


def remove_duplicates(s: str) -> str:
    """Remove duplicate characters, keeping first occurrence.
    Example: remove_duplicates("hello") -> "helo"
    """
    result = ""
    for i in range(len(s)):
        # if result.find(s[i]) == -1:
        if s[i] not in result:
            result += s[i]

    return result


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
