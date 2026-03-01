"""
Problem: Repeated Substring Pattern (LC 459) | Day 10 | Medium
Topic: Strings

Given a string s, check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.

Example 1:
  Input: s = "abab"
  Output: True
  Explanation: It is the substring "ab" repeated twice.

Example 2:
  Input: s = "aba"
  Output: False

Example 3:
  Input: s = "abcabcabcabc"
  Output: True
  Explanation: "abc" repeated four times.

Constraints:
  - 1 <= len(s) <= 10^4
  - s consists of lowercase English letters

Hint: Method 1: Check all possible substring lengths that divide len(s).
      Method 2 (clever): If s is made of repeated substrings, then s will
      appear in (s + s)[1:-1] (the doubled string with first and last
      char removed). This works because the repeated pattern creates
      overlapping occurrences.
Pattern: String Pattern
"""


def repeated_substring_pattern(s: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert repeated_substring_pattern("abab") == True
    assert repeated_substring_pattern("aba") == False
    assert repeated_substring_pattern("abcabcabcabc") == True
    assert repeated_substring_pattern("a") == False
    assert repeated_substring_pattern("aa") == True
    assert repeated_substring_pattern("abaababaab") == True
    print("All tests passed!")
