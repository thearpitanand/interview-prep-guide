"""
Problem: Palindrome Pairs (LC 336) | Day 40 | Hard
Topic: Trie

Given a list of unique words, return all pairs of distinct indices (i, j)
such that the concatenation of words[i] + words[j] is a palindrome.

Example 1:
  Input:  ["abcd", "dcba", "lls", "s", "sssll"]
  Output: [[0,1], [1,0], [3,2], [2,4]]
  Explanation:
    "abcd" + "dcba" = "abcddcba" (palindrome)
    "dcba" + "abcd" = "dcbaabcd" (palindrome)
    "s" + "lls"     = "slls"     (palindrome)
    "lls" + "sssll" = "llssssll" (palindrome)

Example 2:
  Input:  ["bat", "tab", "cat"]
  Output: [[0,1], [1,0]]

Example 3:
  Input:  ["a", ""]
  Output: [[0,1], [1,0]]

Constraints:
  - 1 <= words.length <= 5000
  - 0 <= words[i].length <= 300
  - words[i] consists of lowercase English letters

Hint: Build a trie from reversed words. For each word, traverse the trie.
      At each step, check if the remaining suffix of the word is a palindrome.
      Also check if any remaining suffix in the trie path is a palindrome
      when the word is fully consumed.
Pattern: Trie
"""

from typing import List


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class Solution:
    def palindrome_pairs(self, words: List[str]) -> List[List[int]]:
        pass


# --- Tests ---
if __name__ == "__main__":
    sol = Solution()

    result1 = sol.palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
    expected1 = [[0, 1], [1, 0], [3, 2], [2, 4]]
    assert sorted(result1) == sorted(expected1), f"Got {result1}"

    result2 = sol.palindrome_pairs(["bat", "tab", "cat"])
    expected2 = [[0, 1], [1, 0]]
    assert sorted(result2) == sorted(expected2), f"Got {result2}"

    result3 = sol.palindrome_pairs(["a", ""])
    expected3 = [[0, 1], [1, 0]]
    assert sorted(result3) == sorted(expected3), f"Got {result3}"

    result4 = sol.palindrome_pairs(["a", "b", "c", "ab", "ac", "aa"])
    expected4 = [[3, 0], [1, 3], [4, 0], [2, 4], [5, 0], [0, 5]]
    assert sorted(result4) == sorted(expected4), f"Got {result4}"

    print("All tests passed!")
