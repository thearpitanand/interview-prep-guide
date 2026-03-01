"""
Problem: Find Duplicate Characters in String (GFG) | Optional | Easy
Topic: Strings

Given a string, find all duplicate characters and their counts.

Example 1:
  Input: s = "programming"
  Output: {'r': 2, 'g': 2, 'm': 2}

Constraints:
  - 1 <= len(s) <= 10^5

Hint: Use a frequency counter.
Pattern: Hashing
"""


def duplicate_chars(s: str) -> dict[str, int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert duplicate_chars("programming") == {'r': 2, 'g': 2, 'm': 2}
    assert duplicate_chars("abc") == {}
    assert duplicate_chars("aab") == {'a': 2}
    print("All tests passed!")
