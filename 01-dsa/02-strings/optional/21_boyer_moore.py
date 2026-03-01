"""
Problem: Boyer Moore Pattern Searching (GFG) | Optional | Hard
Topic: Strings

Implement Boyer-Moore string search algorithm. Return index of first occurrence
of pattern in text, or -1.

Example 1:
  Input: text = "ABAAABCD", pattern = "ABC"
  Output: 4

Constraints:
  - 1 <= len(text) <= 10^5

Hint: Use bad character heuristic for skipping.
Pattern: Boyer-Moore Algorithm
"""


def boyer_moore(text: str, pattern: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert boyer_moore("ABAAABCD", "ABC") == 4
    assert boyer_moore("hello", "ll") == 2
    assert boyer_moore("abc", "d") == -1
    print("All tests passed!")
