"""
Problem: Implement Trie (LC 208) | Day 40 | Easy
Topic: Trie

Implement a trie with insert, search, and startsWith methods.

Example:
  trie = Trie()
  trie.insert("apple")
  trie.search("apple")   -> True
  trie.search("app")     -> False
  trie.startsWith("app") -> True
  trie.insert("app")
  trie.search("app")     -> True

Constraints:
  - 1 <= word.length, prefix.length <= 2000
  - word and prefix consist of lowercase English letters

Hint: Use a dict of children + is_end boolean at each node.
Pattern: Basic Trie
"""


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass


# --- Tests ---
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.starts_with("app") == True
    trie.insert("app")
    assert trie.search("app") == True
    assert trie.search("banana") == False
    assert trie.starts_with("ban") == False
    print("All tests passed!")
