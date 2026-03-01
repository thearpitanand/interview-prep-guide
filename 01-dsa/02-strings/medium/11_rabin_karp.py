"""
Problem: Rabin-Karp Algorithm (GFG) | Day 11 | Medium
Topic: Strings

Implement Rabin-Karp pattern searching algorithm using rolling hash.
Return the index of the first occurrence of pattern in text, or -1 if not found.

Example 1:
  Input: text = "abcxabcdabcdabcy", pattern = "abcdabcy"
  Output: 8

Constraints:
  - 1 <= text.length <= 10^5
  - 1 <= pattern.length <= text.length

Hint: Use rolling hash to compute hash of each window in O(1). Verify on hash match.
Pattern: Rabin-Karp / Rolling Hash
"""


def rabin_karp(text: str, pattern: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert rabin_karp("abcxabcdabcdabcy", "abcdabcy") == 8
    assert rabin_karp("hello", "ll") == 2
    assert rabin_karp("abc", "d") == -1
    assert rabin_karp("aaaa", "aa") == 0
    print("All tests passed!")
