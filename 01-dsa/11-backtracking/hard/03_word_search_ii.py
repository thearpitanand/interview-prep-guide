"""
Word Search II (LC 212)

Day: 32 | Difficulty: Hard | Pattern: Trie + Backtracking

Given an m x n board of characters and a list of strings words, return all
words found on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

Examples:
    Input: board = [["o","a","a","n"],
                    ["e","t","a","e"],
                    ["i","h","k","r"],
                    ["i","f","l","v"]],
           words = ["oath","pea","eat","rain"]
    Output: ["eat", "oath"]

    Input: board = [["a","b"],
                    ["c","d"]],
           words = ["abcb"]
    Output: []

Constraints:
    - m == board.length
    - n == board[i].length
    - 1 <= m, n <= 12
    - board[i][j] is a lowercase English letter
    - 1 <= words.length <= 3 * 10^4
    - 1 <= words[i].length <= 10
    - words[i] consists of lowercase English letters
    - All the strings of words are unique

Hint:
    Build a Trie from the word list. Then DFS from each cell on the board,
    traversing the Trie simultaneously. If the current Trie node has a word,
    add it to results. Prune: if there's no Trie child for the current cell
    letter, stop that branch. Optimization: remove found words from the Trie
    to avoid duplicates and reduce search space.

Pattern: Trie + Backtracking on grid. The Trie replaces checking each word
individually, turning O(words * cells * 4^L) into a single traversal that
finds all words simultaneously.
"""

from typing import List


class TrieNode:
    """Trie node for word search."""

    def __init__(self):
        self.children = {}
        self.word = None  # Store complete word at leaf nodes


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """Find all words from the dictionary that exist on the board."""
    pass


def find_words_optimized(board: List[List[str]], words: List[str]) -> List[str]:
    """Optimized: prune Trie nodes after finding words."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard example
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    result = sorted(find_words(board, words))
    expected = sorted(["eat", "oath"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: No words found
    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]
    result = find_words(board2, words2)
    assert result == [], f"Expected [], got {result}"

    # Test 3: Single cell board
    board3 = [["a"]]
    words3 = ["a"]
    result = find_words(board3, words3)
    assert result == ["a"], f"Expected ['a'], got {result}"

    # Test 4: All words found
    board4 = [["a", "b"], ["c", "d"]]
    words4 = ["ab", "cd", "ac"]
    result = sorted(find_words(board4, words4))
    expected = sorted(["ab", "cd", "ac"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 5: Overlapping words (shared prefix)
    board5 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words5 = ["oath", "oat"]
    result = sorted(find_words(board5, words5))
    expected = sorted(["oath", "oat"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 6: Optimized version
    board6 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words6 = ["oath", "pea", "eat", "rain"]
    result = sorted(find_words_optimized(board6, words6))
    expected = sorted(["eat", "oath"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 7: No duplicate results
    board7 = [["a", "a"]]
    words7 = ["a"]
    result = find_words(board7, words7)
    assert result == ["a"], f"Expected ['a'], got {result} (should not have duplicates)"

    print("All tests passed!")
