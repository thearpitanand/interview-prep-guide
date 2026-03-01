"""
Problem: Word Break
Day: 37 | Difficulty: Medium | Topic: 1D DP
Link: https://leetcode.com/problems/word-break/

Description:
    Given a string s and a dictionary of strings wordDict, return True if s
    can be segmented into a space-separated sequence of one or more dictionary
    words. The same word in the dictionary may be reused multiple times.

Examples:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: True
    Explanation: "leetcode" can be segmented as "leet code".

    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: True
    Explanation: "apple pen apple". Note "apple" is reused.

    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: False

Constraints:
    - 1 <= s.length <= 300
    - 1 <= wordDict.length <= 1000
    - 1 <= wordDict[i].length <= 20
    - s and wordDict[i] consist of only lowercase English letters

Hint:
    dp[i] = True if s[0:i] can be segmented using dictionary words.
    dp[0] = True (empty string). For each position i, check all positions
    j < i: if dp[j] is True and s[j:i] is in the dictionary, then dp[i] = True.
    Convert wordDict to a set for O(1) lookup.

Pattern: 1D DP on string. dp[i] depends on all dp[j] where j < i and
    s[j:i] is a valid word. O(n^2 * k) where k is max word length.
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s": "leetcode", "word_dict": ["leet", "code"], "expected": True},
        {"s": "applepenapple", "word_dict": ["apple", "pen"], "expected": True},
        {"s": "catsandog", "word_dict": ["cats", "dog", "sand", "and", "cat"], "expected": False},
        {"s": "a", "word_dict": ["a"], "expected": True},
        {"s": "ab", "word_dict": ["a", "b"], "expected": True},
        {"s": "aaaaaaa", "word_dict": ["aaaa", "aaa"], "expected": True},
    ]

    for i, t in enumerate(tests):
        result = word_break(t["s"], t["word_dict"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
