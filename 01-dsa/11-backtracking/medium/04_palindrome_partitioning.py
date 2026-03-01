"""
Palindrome Partitioning (LC 131)

Day: 32 | Difficulty: Medium | Pattern: Backtracking - String Partitioning

Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

Examples:
    Input: s = "aab"
    Output: [["a", "a", "b"], ["aa", "b"]]

    Input: s = "a"
    Output: [["a"]]

    Input: s = "aba"
    Output: [["a", "b", "a"], ["aba"]]

Constraints:
    - 1 <= s.length <= 16
    - s contains only lowercase English letters

Hint:
    At each position, try all possible substrings starting from that position.
    If the substring is a palindrome, add it to the current partition and recurse
    on the remaining string. When you reach the end, you've found a valid partition.
    Optimization: precompute a palindrome lookup table using DP.

Pattern: Backtracking on string partitions. At index i, try every end position
j > i. If s[i:j] is a palindrome, include it and recurse from j.
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    """Return all palindrome partitions of the string."""
    pass


def partition_with_dp(s: str) -> List[List[str]]:
    """Optimized: precompute palindrome table, then backtrack."""
    pass


# --- Helper ---

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    return s == s[::-1]


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Basic case
    result = sorted(partition("aab"))
    expected = sorted([["a", "a", "b"], ["aa", "b"]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: Single character
    result = partition("a")
    assert result == [["a"]], f"Expected [['a']], got {result}"

    # Test 3: Palindrome string
    result = sorted(partition("aba"))
    expected = sorted([["a", "b", "a"], ["aba"]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 4: All same characters
    result = sorted(partition("aaa"))
    expected = sorted([["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 5: No multi-char palindromes
    result = partition("abc")
    assert result == [["a", "b", "c"]], f"Expected [['a', 'b', 'c']], got {result}"

    # Test 6: DP-optimized version
    result = sorted(partition_with_dp("aab"))
    expected = sorted([["a", "a", "b"], ["aa", "b"]])
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")
