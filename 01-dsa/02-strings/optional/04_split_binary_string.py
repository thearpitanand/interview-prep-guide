"""
Problem: Split Binary String with Equal 0s and 1s (LC 1221) | Optional | Easy
Topic: Strings

Given a binary string, return the maximum number of non-empty substrings
you can split it into such that each has equal 0s and 1s.

Example 1:
  Input: s = "0100110101"
  Output: 4

Constraints:
  - 2 <= s.length <= 1000
  - s[i] is '0' or '1'
  - Equal number of 0s and 1s in s

Hint: Track count of 0s and 1s; every time they're equal, that's a valid split.
Pattern: Counting
"""


def max_balanced_splits(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_balanced_splits("0100110101") == 4
    assert max_balanced_splits("10") == 1
    assert max_balanced_splits("0011") == 1
    print("All tests passed!")
