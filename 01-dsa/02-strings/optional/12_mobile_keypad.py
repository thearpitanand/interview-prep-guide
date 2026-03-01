"""
Problem: Sentence to Mobile Keypad Sequence (GFG) | Optional | Medium
Topic: Strings

Convert a sentence to the sequence of key presses on old mobile phone keypad.
2=abc, 3=def, 4=ghi, 5=jkl, 6=mno, 7=pqrs, 8=tuv, 9=wxyz.

Example 1:
  Input: s = "hello"
  Output: "4433555555666"

Constraints:
  - 1 <= len(s) <= 10^4
  - Lowercase English letters and spaces

Hint: Map each character to its key presses.
Pattern: Hash Map
"""


def mobile_keypad_sequence(s: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert mobile_keypad_sequence("hello") == "4433555555666"
    assert mobile_keypad_sequence("a") == "2"
    print("All tests passed!")
