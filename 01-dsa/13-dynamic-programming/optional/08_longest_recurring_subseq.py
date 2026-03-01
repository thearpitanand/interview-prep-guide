"""
Problem: Longest Repeating Subsequence (GFG) | Optional | Medium
Topic: Dynamic Programming

Find the length of the longest subsequence that repeats itself (same chars at different indices).

Example 1:
  Input: s = "aabb"
  Output: 2  # "ab" repeats

Constraints:
  - 1 <= len(s) <= 10^3

Hint: LCS of s with itself, but with constraint i != j.
Pattern: LCS variant
"""


def longest_repeating_subseq(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_repeating_subseq("aabb") == 2
    assert longest_repeating_subseq("aab") == 1
    assert longest_repeating_subseq("abc") == 0
    print("All tests passed!")
