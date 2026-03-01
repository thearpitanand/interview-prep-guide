"""
Problem: Replace Words (LC 648) | Day 40 | Medium
Topic: Trie

Given a dictionary of root words and a sentence, replace all successors
(words that have a root as a prefix) with the root forming it. If a word
has multiple roots, replace it with the shortest one.

Example 1:
  Input:  dictionary = ["cat", "bat", "rat"]
          sentence = "the cattle was rattled by the battery"
  Output: "the cat was rat by the bat"

Example 2:
  Input:  dictionary = ["a", "b", "c"]
          sentence = "aadsfasf absbd bbab cadsfabd"
  Output: "a]a b c"

Example 3:
  Input:  dictionary = ["a", "aa", "aaa", "aaaa"]
          sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
  Output: "a a a a a a a a bbb baba a"

Constraints:
  - 1 <= dictionary.length <= 1000
  - 1 <= dictionary[i].length <= 100
  - dictionary[i] consists of only lowercase letters
  - 1 <= sentence.length <= 10^6
  - sentence consists of only lowercase letters and spaces

Hint: Build a trie from the dictionary roots. For each word in the sentence,
      walk the trie; if you reach an is_end node, use that prefix as the
      replacement. Otherwise, keep the original word.
Pattern: Trie Prefix Search
"""

from typing import List


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class Solution:
    def replace_words(self, dictionary: List[str], sentence: str) -> str:
        pass


# --- Tests ---
if __name__ == "__main__":
    sol = Solution()

    assert sol.replace_words(
        ["cat", "bat", "rat"],
        "the cattle was rattled by the battery"
    ) == "the cat was rat by the bat"

    assert sol.replace_words(
        ["a", "b", "c"],
        "aadsfasf absbd bbab cadsfabd"
    ) == "a a b c"

    assert sol.replace_words(
        ["a", "aa", "aaa", "aaaa"],
        "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    ) == "a a a a a a a a bbb baba a"

    assert sol.replace_words(
        ["catt", "cat", "bat", "rat"],
        "the cattle was rattled by the battery"
    ) == "the cat was rat by the bat"

    assert sol.replace_words([], "nothing changes here") == "nothing changes here"

    print("All tests passed!")
