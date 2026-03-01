"""
Problem: Longest Substring Without Repeating Characters (LC 3) | Day 10 | Medium
Topic: Strings

Given a string s, find the length of the longest substring without
repeating characters.

Example 1:
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.

Example 2:
  Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.

Example 3:
  Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.

Constraints:
  - 0 <= len(s) <= 5 * 10^4
  - s consists of English letters, digits, symbols and spaces

Hint: Use a sliding window with a set or hash map. Expand the right pointer.
      When a duplicate is found, shrink from the left until the duplicate
      is removed. Track the maximum window size.
Pattern: Sliding Window
"""


def length_of_longest_substring(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("au") == 2
    print("All tests passed!")
