"""
Problem: Palindrome Partitioning (LC 131) | Smart-DSA Day 34 | Medium
Pattern: Backtracking + String
Time target: 30 minutes

Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

Example 1:
  Input: s = "aab"
  Output: [["a","a","b"],["aa","b"]]

Example 2:
  Input: s = "a"
  Output: [["a"]]

Constraints:
  - 1 <= s.length <= 16
  - s consists only of lowercase English letters.

Hint (⚠ read only after time budget is blown):
  Backtrack with a start index. At each step, try every suffix s[start:end+1].
  If it is a palindrome, add it to the path and recurse from end+1. When start
  reaches the end of the string, record the path.
"""


def partition(s: str) -> list[list[str]]:
    pass


if __name__ == "__main__":
    result1 = partition("aab")
    assert sorted(map(tuple, result1)) == sorted(map(tuple, [["a", "a", "b"], ["aa", "b"]]))

    result2 = partition("a")
    assert result2 == [["a"]]

    result3 = partition("aa")
    assert sorted(map(tuple, result3)) == sorted(map(tuple, [["a", "a"], ["aa"]]))
    print("All tests passed!")
