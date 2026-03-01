"""
Exercise: File I/O and String Processing | Day 2
Topic: Python Basics

Practice string processing patterns common in coding interviews.
(No actual file I/O needed - we simulate with strings)

Instructions: Implement each function below.
"""


def parse_csv_line(line: str) -> list[str]:
    """Parse a CSV line into a list of values.
    Example: parse_csv_line("a,b,c") -> ['a', 'b', 'c']
    """
    pass


def format_table(headers: list[str], rows: list[list[str]]) -> str:
    """Format data as a simple text table.
    Each column width = max(header, longest value in column).
    Left-align all values. Separate header with dashes.

    Example:
    format_table(["Name", "Age"], [["Alice", "30"], ["Bob", "25"]])
    ->
    Name  Age
    ----  ---
    Alice 30
    Bob   25
    """
    pass


def count_lines(text: str) -> dict:
    """Count total lines, blank lines, and non-blank lines.
    Return {'total': x, 'blank': y, 'non_blank': z}
    """
    pass


def extract_numbers(text: str) -> list[int]:
    """Extract all integers from a string.
    Example: extract_numbers("I have 3 cats and 2 dogs") -> [3, 2]
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert parse_csv_line("a,b,c") == ['a', 'b', 'c']
    assert parse_csv_line("hello,world") == ['hello', 'world']

    result = count_lines("hello\n\nworld\n")
    assert result['total'] == 3
    assert result['blank'] == 1
    assert result['non_blank'] == 2

    assert extract_numbers("I have 3 cats and 2 dogs") == [3, 2]
    assert extract_numbers("no numbers here") == []
    print("All tests passed!")
