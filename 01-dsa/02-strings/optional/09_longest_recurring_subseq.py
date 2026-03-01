"""
Problem: Longest Recurring Subsequence (GFG) | Optional | Medium
Topic: Strings

Given a string, find the length of the longest subsequence that repeats
itself (characters at different indices).

Example 1:
  Input: s = "aab"
  Output: 1  # "a" repeats (indices 0 and 1)

Example 2:
  Input: s = "aabb"
  Output: 2  # "ab" repeats

Constraints:
  - 1 <= len(s) <= 10^3

Hint: LCS of string with itself, but with condition i != j.
Pattern: Dynamic Programming (LCS variant)
"""


def longest_recurring_subseq(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_recurring_subseq("aab") == 1
    assert longest_recurring_subseq("aabb") == 2
    assert longest_recurring_subseq("abc") == 0
    print("All tests passed!")
