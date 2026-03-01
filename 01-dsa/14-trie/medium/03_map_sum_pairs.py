"""
Problem: Map Sum Pairs (LC 677) | Day 40 | Medium
Topic: Trie

Design a map that allows you to:
  - insert(key, val): Insert a key-value pair. If the key already exists,
                      the original value is replaced with the new one.
  - sum(prefix):      Return the sum of all values whose key starts with
                      the given prefix.

Example:
  ms = MapSum()
  ms.insert("apple", 3)
  ms.sum("ap")           -> 3
  ms.insert("app", 2)
  ms.sum("ap")           -> 5
  ms.insert("apple", 2)  # update "apple" from 3 to 2
  ms.sum("ap")           -> 4  (apple=2 + app=2)

Constraints:
  - 1 <= key.length, prefix.length <= 50
  - key and prefix consist of only lowercase English letters
  - 1 <= val <= 1000
  - At most 50 calls to insert and sum

Hint: Use a trie where each node stores a value. For sum, navigate to the
      prefix node and DFS to sum all values below it. Store a separate
      hashmap to handle key updates (subtract old value, add new value).
Pattern: Trie Prefix Search
"""


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class MapSum:
    def __init__(self):
        pass

    def insert(self, key: str, val: int) -> None:
        pass

    def sum(self, prefix: str) -> int:
        pass


# --- Tests ---
if __name__ == "__main__":
    ms = MapSum()
    ms.insert("apple", 3)
    assert ms.sum("ap") == 3
    ms.insert("app", 2)
    assert ms.sum("ap") == 5
    ms.insert("apple", 2)  # update apple from 3 to 2
    assert ms.sum("ap") == 4
    assert ms.sum("b") == 0
    assert ms.sum("apple") == 2
    assert ms.sum("app") == 4

    ms2 = MapSum()
    ms2.insert("a", 10)
    ms2.insert("ab", 20)
    ms2.insert("abc", 30)
    assert ms2.sum("a") == 60
    assert ms2.sum("ab") == 50
    assert ms2.sum("abc") == 30
    assert ms2.sum("z") == 0

    print("All tests passed!")
