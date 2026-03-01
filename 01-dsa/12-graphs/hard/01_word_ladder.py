"""
Word Ladder (LC 127)

Day: 35 | Difficulty: Hard | Pattern: BFS

A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence beginWord -> s1 -> s2 -> ... -> sk such that:
  - Every adjacent pair of words differs by a single letter.
  - Every si for 1 <= i <= k is in wordList. (beginWord does not need to be.)
  - sk == endWord

Given two words beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.

Examples:
    Input: beginWord="hit", endWord="cog",
           wordList=["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" (5 words)

    Input: beginWord="hit", endWord="cog",
           wordList=["hot","dot","dog","lot","log"]
    Output: 0
    Explanation: endWord "cog" is not in wordList.

Constraints:
    - 1 <= beginWord.length <= 10
    - endWord.length == beginWord.length
    - 1 <= wordList.length <= 5000
    - wordList[i].length == beginWord.length
    - beginWord, endWord, and wordList[i] consist of lowercase English letters
    - beginWord != endWord
    - All words in wordList are unique

Hint:
    Model this as a graph problem: each word is a node, and an edge exists
    between two words that differ by exactly one letter. Use BFS for shortest
    path. Optimization: use wildcard patterns (e.g., "h*t" matches "hot",
    "hit") to find neighbors efficiently instead of comparing all pairs.

Pattern: BFS shortest path - each word is a node, edges connect words that
differ by one letter. BFS gives the shortest transformation sequence.
"""

from collections import defaultdict, deque
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """BFS approach with wildcard pattern optimization."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case
    result = ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    assert result == 5, f"Expected 5, got {result}"

    # Test 2: End word not in list
    result = ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    assert result == 0, f"Expected 0, got {result}"

    # Test 3: Direct transformation
    result = ladder_length("hot", "dot", ["dot"])
    assert result == 2, f"Expected 2, got {result}"

    # Test 4: No possible transformation
    result = ladder_length("abc", "xyz", ["abd", "xyd"])
    assert result == 0, f"Expected 0, got {result}"

    # Test 5: Longer chain
    result = ladder_length("a", "c", ["a", "b", "c"])
    assert result == 2, f"Expected 2, got {result}"

    print("All tests passed!")
