"""
Problem: Word Break (LC 139) | Smart-DSA Day 44 | Medium
Pattern: Dynamic Programming — 1D String DP
Time target: 30 minutes

Given a string s and a list of strings wordDict, return True if s can be
segmented into a space-separated sequence of one or more words from wordDict.
Words in wordDict can be reused any number of times.

Example 1:
  Input: s = "leetcode", wordDict = ["leet", "code"]
  Output: True  ("leet code")

Example 2:
  Input: s = "applepenapple", wordDict = ["apple", "pen"]
  Output: True  ("apple pen apple")

Example 3:
  Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
  Output: False

Constraints:
  - 1 <= s.length <= 300
  - 1 <= wordDict.length <= 1000
  - 1 <= wordDict[i].length <= 20

Hint (⚠ read only after time budget is blown):
  dp[i] = True if s[:i] can be segmented. dp[0] = True (empty string).
  For each i, check every j < i: if dp[j] is True and s[j:i] is in the
  word set, set dp[i] = True. Answer is dp[len(s)].
"""


def word_break(s: str, wordDict: list[str]) -> bool:
    pass


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert word_break("a", ["a"]) is True
    assert word_break("ab", ["a", "b"]) is True
    print("All tests passed!")
