"""
Problem: Longest Common Prefix using Trie (LC 14 variant) | Day 40 | Easy
Topic: Trie

Given an array of strings, find the longest common prefix using a Trie approach.
Insert all words into a trie, then walk from the root following single-child
nodes that are not end-of-word markers.

Example 1:
  Input:  ["flower", "flow", "flight"]
  Output: "fl"

Example 2:
  Input:  ["dog", "racecar", "car"]
  Output: ""

Example 3:
  Input:  ["interspecies", "interstellar", "interstate"]
  Output: "inters"

Constraints:
  - 1 <= strs.length <= 200
  - 0 <= strs[i].length <= 200
  - strs[i] consists of only lowercase English letters

Hint: Build a trie from all words. Walk from root; the common prefix ends
      when a node has more than one child or is marked as end of a word.
Pattern: Basic Trie
"""

from typing import List


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        pass


# --- Tests ---
if __name__ == "__main__":
    sol = Solution()

    assert sol.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert sol.longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"
    assert sol.longest_common_prefix(["a"]) == "a"
    assert sol.longest_common_prefix([""]) == ""
    assert sol.longest_common_prefix(["", "b"]) == ""
    assert sol.longest_common_prefix(["abc", "abc", "abc"]) == "abc"

    print("All tests passed!")
