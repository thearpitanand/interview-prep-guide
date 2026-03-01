"""
Problem: Check if String is Rotation of Another (LC 796) | Optional | Easy
Topic: Strings

Given two strings s and goal, return true if s can become goal after some
number of shifts/rotations.

Example 1:
  Input: s = "abcde", goal = "cdeab"
  Output: True

Constraints:
  - 1 <= s.length, goal.length <= 100

Hint: s is a rotation of goal iff goal is a substring of s+s (and same length).
Pattern: String Concatenation
"""


def is_rotation(s: str, goal: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_rotation("abcde", "cdeab") == True
    assert is_rotation("abcde", "abced") == False
    assert is_rotation("a", "a") == True
    print("All tests passed!")
