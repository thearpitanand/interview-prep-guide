"""
Problem: Group Anagrams (LC 49) | Day 10 | Medium
Topic: Strings

Given an array of strings strs, group the anagrams together. You can
return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, using all the original letters exactly once.

Example 1:
  Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
  Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Example 2:
  Input: strs = [""]
  Output: [[""]]

Example 3:
  Input: strs = ["a"]
  Output: [["a"]]

Constraints:
  - 1 <= len(strs) <= 10^4
  - 0 <= len(strs[i]) <= 100
  - strs[i] consists of lowercase English letters

Hint: Use sorted string as a hash key (anagrams produce the same sorted string).
      Alternatively, use a tuple of 26 character counts as the key for O(n*k)
      where k is the max string length (avoids the n*k*log(k) sorting cost).
Pattern: Hash Map
"""
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort inner lists and outer list for comparison
    result = sorted([sorted(g) for g in result])
    expected = sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
    assert result == expected

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed!")
