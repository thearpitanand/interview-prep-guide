"""
Problem: Scramble String
Day: 39 | Difficulty: Hard | Topic: String DP / Recursion + Memo
Link: https://leetcode.com/problems/scramble-string/

Description:
    We can scramble a string s to get a string t using the following algorithm:
    1. If the length of the string is 1, stop.
    2. If the length of the string is > 1, do the following:
       - Split the string into two non-empty substrings at a random index.
       - Randomly decide to swap the two substrings or keep them in order.
       - Apply step 1 recursively on each of the two substrings.
    Given two strings s1 and s2 of the same length, return True if s2 is a
    scrambled string of s1, otherwise return False.

Examples:
    Input: s1 = "great", s2 = "rgeat"
    Output: True
    Explanation: "great" -> split at index 2 -> "gr" + "eat"
    -> swap -> "eat" + "gr" -> "rg" (scramble "gr") + "eat" = "rgeat"

    Input: s1 = "abcde", s2 = "caebd"
    Output: False

    Input: s1 = "a", s2 = "a"
    Output: True

Constraints:
    - s1.length == s2.length
    - 1 <= s1.length <= 30
    - s1 and s2 consist of lowercase English letters

Hint:
    Use recursion with memoization. For each split point i (1 to len-1):
    1. No swap: isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])
    2. Swap: isScramble(s1[:i], s2[n-i:]) and isScramble(s1[i:], s2[:n-i])
    Prune: if sorted characters don't match, return False immediately.
    Memoize with (s1, s2) as key.

Pattern: Recursive DP with memoization. Try all split points, with and
    without swap. Prune early using character frequency check.
"""


def is_scramble(s1: str, s2: str) -> bool:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s1": "great", "s2": "rgeat", "expected": True},
        {"s1": "abcde", "s2": "caebd", "expected": False},
        {"s1": "a", "s2": "a", "expected": True},
        {"s1": "ab", "s2": "ba", "expected": True},
        {"s1": "ab", "s2": "ab", "expected": True},
        {"s1": "abc", "s2": "bca", "expected": True},
        {"s1": "abcd", "s2": "bdac", "expected": False},
    ]

    for i, t in enumerate(tests):
        result = is_scramble(t["s1"], t["s2"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
