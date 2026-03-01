"""
Problem: Reverse String (LC 344) | Day 4 | Easy
Topic: Arrays

Write a function that reverses a list of characters in-place.

Example 1:
  Input: s = ["h","e","l","l","o"]
  Output: ["o","l","l","e","h"]

Example 2:
  Input: s = ["H","a","n","n","a","h"]
  Output: ["h","a","n","n","a","H"]

Constraints:
  - 1 <= s.length <= 10^5

Hint: Use two pointers from both ends.
Pattern: Two Pointers
"""


def reverse_string(s: list[str]) -> None:
    # Write your solution here (modify in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    s1 = ["h", "e", "l", "l", "o"]
    reverse_string(s1)
    assert s1 == ["o", "l", "l", "e", "h"]

    s2 = ["H", "a", "n", "n", "a", "h"]
    reverse_string(s2)
    assert s2 == ["h", "a", "n", "n", "a", "H"]
    print("All tests passed!")
