"""
Exercise: Control Flow | Day 1
Topic: Python Basics

Practice if/elif/else statements and conditional logic.

Instructions: Implement each function below.
"""


def fizzbuzz(n: int) -> str:
    """Return 'Fizz' if n is divisible by 3, 'Buzz' if by 5,
    'FizzBuzz' if by both, otherwise return str(n).
    """
    result = ""
    if n % 3 == 0:
        result += "Fizz"

    if n % 5 == 0:
        result += "Buzz"

    if len(result) == 0:
        result = str(n)

    return result


def grade(score: int) -> str:
    """Return letter grade: A (90-100), B (80-89), C (70-79),
    D (60-69), F (below 60).
    """

    """
    # Attempt 1
    
    if 90 <= score <= 100:
        return "A"
    if 80 <= score <= 89:
        return "B"
    if 70 <= score <= 79:
        return "C"
    if 60 <= score <= 69:
        return "D"
    return "F"
    """

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def absolute_value(n: int) -> int:
    """Return absolute value without using abs()."""
    if n < 0:
        return n - (2 * n)
        # -5 - (2 * -5)
        # -5 - (-10)
        # -5 + 10
        # 5
    return n


def max_of_three(a: int, b: int, c: int) -> int:
    """Return the maximum of three numbers without using max()."""

    if (a >= b) and (a >= c):
        return a

    if (b >= a) and (b >= c):
        return b

    return c


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year.
    Leap year: divisible by 4, but not 100, unless also by 400.
    """
    if year % 4 == 0:
        if not year % 100 == 0:
            return True

        if year % 400 == 0:
            return True

        return False

    return False


# --- Tests ---
if __name__ == "__main__":
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == "7"

    assert grade(95) == "A"
    assert grade(85) == "B"
    assert grade(55) == "F"

    assert absolute_value(-5) == 5
    assert absolute_value(3) == 3

    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(3, 1, 2) == 3

    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2024) == True
    print("All tests passed!")
