"""
Problem: Design Add and Search Words Data Structure (LC 211) | Day 40 | Medium
Topic: Trie + DFS

Design a data structure that supports adding new words and searching for words
where '.' can match any single letter.

Implement:
  - WordDictionary()       -> Initialize the object
  - addWord(word)          -> Add word to the data structure
  - search(word)           -> Return True if any previously added word matches.
                              '.' can match any letter.

Example:
  wd = WordDictionary()
  wd.addWord("bad")
  wd.addWord("dad")
  wd.addWord("mad")
  wd.search("pad")  -> False
  wd.search("bad")  -> True
  wd.search(".ad")  -> True
  wd.search("b..")  -> True

Constraints:
  - 1 <= word.length <= 25
  - word in addWord consists of lowercase English letters
  - word in search consists of '.' or lowercase English letters
  - At most 10^4 calls to addWord and search

Hint: Use a trie for storage. For search, when encountering '.', recursively
      try all children of the current node using DFS.
Pattern: Trie + DFS
"""


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class WordDictionary:
    def __init__(self):
        pass

    def add_word(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


# --- Tests ---
if __name__ == "__main__":
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")

    assert wd.search("pad") == False
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("b..") == True
    assert wd.search("b.d") == True
    assert wd.search("b.a") == False
    assert wd.search("...") == True
    assert wd.search("....") == False
    assert wd.search("") == False

    wd.add_word("a")
    assert wd.search(".") == True
    assert wd.search("a") == True

    print("All tests passed!")
