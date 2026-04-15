"""
Problem: Group Anagrams (LC 49) | Smart-DSA Day 2 | Medium
Pattern: Arrays & Hashing
Time target: 25 minutes

Given an array of strings, group the anagrams together. Return results in any
order, with each group in any order.

Example 1:
  Input: strs = ["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
  Input: strs = [""]
  Output: [[""]]

Constraints:
  - 1 <= strs.length <= 10^4
  - 0 <= strs[i].length <= 100
  - strs[i] consists of lowercase English letters.

Hint (⚠ read only after time budget is blown):
  Use sorted(word) as the hash map key — all anagrams share the same sorted
  form. Group words by that key.
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    pass


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted([sorted(g) for g in result])
    assert normalized == sorted([sorted(g) for g in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed!")
