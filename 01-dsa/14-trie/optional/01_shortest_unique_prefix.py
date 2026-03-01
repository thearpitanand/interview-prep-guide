"""
Problem: Shortest Unique Prefix for Every Word (GFG) | Optional | Medium
Topic: Trie

Given an array of words, find the shortest unique prefix for each word such
that it uniquely identifies the word.

Example 1:
  Input: words = ["zebra", "dog", "duck", "dove"]
  Output: ["z", "dog", "du", "dov"]

Constraints:
  - 1 <= n <= 10^4

Hint: Build trie. For each word, the shortest prefix is where the count of passing words becomes 1.
Pattern: Trie
"""


def shortest_unique_prefix(words: list[str]) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert shortest_unique_prefix(["zebra", "dog", "duck", "dove"]) == ["z", "dog", "du", "dov"]
    assert shortest_unique_prefix(["apple", "banana"]) == ["a", "b"]
    print("All tests passed!")
