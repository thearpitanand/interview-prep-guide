"""
Problem: Smallest Window Containing All Characters (GFG) | Optional | Medium
Topic: Strings

Given two strings s and p, find the smallest window in s that contains all
characters of p (including duplicates).

Example 1:
  Input: s = "ADOBECODEBANC", p = "ABC"
  Output: "BANC"

Constraints:
  - 1 <= len(s), len(p) <= 10^5

Hint: Sliding window with character frequency tracking.
Pattern: Sliding Window
"""


def smallest_window(s: str, p: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert smallest_window("ADOBECODEBANC", "ABC") == "BANC"
    assert smallest_window("a", "a") == "a"
    print("All tests passed!")
