"""
Problem: Word Ladder (LC 127) | Smart-DSA Day 39 | Hard
Pattern: BFS Shortest Path (Implicit Graph)
Time target: 40 minutes

Given a beginWord, an endWord, and a wordList, return the number of words in
the shortest transformation sequence from beginWord to endWord, where each
transformed word must exist in wordList and differ from the previous word by
exactly one letter. Return 0 if no such sequence exists.

Example 1:
  Input: beginWord = "hit", endWord = "cog",
         wordList = ["hot","dot","dog","lot","log","cog"]
  Output: 5
  Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

Example 2:
  Input: beginWord = "hit", endWord = "cog",
         wordList = ["hot","dot","dog","lot","log"]
  Output: 0
  (endWord not in wordList)

Constraints:
  - 1 <= beginWord.length <= 10
  - beginWord and endWord have the same length.
  - 1 <= wordList.length <= 5000
  - All words consist of lowercase English letters.

Hint (⚠ read only after time budget is blown):
  BFS where each node is a word. Neighbors are words in wordList that differ
  by one character. Convert wordList to a set for O(1) lookups. Remove visited
  words from the set to avoid revisiting. Track BFS level as transformation
  length.
"""
from collections import deque


def ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
    pass


if __name__ == "__main__":
    assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert ladder_length("a", "c", ["a","b","c"]) == 2
    print("All tests passed!")
