"""
Problem: KMP Pattern Matching (LC 28) | Day 11 | Medium
Topic: Strings

Implement the KMP (Knuth-Morris-Pratt) string matching algorithm.
Return the index of the first occurrence of pattern in text, or -1 if not found.

Example 1:
  Input: text = "aaaxaaaa", pattern = "aaaa"
  Output: 4

Constraints:
  - 1 <= text.length <= 10^4
  - 1 <= pattern.length <= text.length
  - Both consist of lowercase English letters

Hint: Build the LPS (Longest Proper Prefix which is also Suffix) array first.
Pattern: KMP Algorithm
"""


def kmp_search(text: str, pattern: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert kmp_search("aaaxaaaa", "aaaa") == 4
    assert kmp_search("hello", "ll") == 2
    assert kmp_search("abc", "d") == -1
    assert kmp_search("aabaaabaaac", "aabaaac") == 4
    print("All tests passed!")
