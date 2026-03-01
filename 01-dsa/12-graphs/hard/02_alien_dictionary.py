"""
Alien Dictionary (LC 269 variant)

Day: 35 | Difficulty: Hard | Pattern: Topological Sort

There is a new alien language that uses the English alphabet. However, the
order of the letters is unknown to you. You are given a list of strings words
from the alien language's dictionary, where the strings are sorted
lexicographically by the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return
an empty string. If there are multiple valid orderings, return any of them.

Examples:
    Input: words=["wrt","wrf","er","ett","rftt"]
    Output: "wertf"
    Explanation: From "wrt" vs "wrf" -> t before f
                 From "wrf" vs "er" -> w before e
                 From "er" vs "ett" -> r before t
                 From "ett" vs "rftt" -> e before r

    Input: words=["z","x"]
    Output: "zx"

    Input: words=["z","x","z"]
    Output: ""
    Explanation: Invalid ordering (z before x AND x before z is impossible).

Constraints:
    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 100
    - words[i] consists of only lowercase English letters
    - The input is such that a valid ordering exists (except invalid cases)

Hint:
    Compare consecutive words to extract ordering rules (edges in a DAG).
    For each pair of adjacent words, find the first differing character --
    this gives a directed edge. Then use topological sort on the resulting
    graph. Watch out for: (1) a longer word before its prefix (invalid),
    (2) cycles (invalid).

Pattern: Topological Sort on character ordering - extract ordering constraints
from consecutive word pairs and topologically sort the characters.
"""

from collections import defaultdict, deque
from typing import List


def alien_order(words: List[str]) -> str:
    """Derive alien alphabet order using topological sort."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case
    result = alien_order(["wrt", "wrf", "er", "ett", "rftt"])
    assert result == "wertf", f"Expected 'wertf', got '{result}'"

    # Test 2: Simple two-word case
    result = alien_order(["z", "x"])
    assert result == "zx", f"Expected 'zx', got '{result}'"

    # Test 3: Invalid ordering (cycle)
    result = alien_order(["z", "x", "z"])
    assert result == "", f"Expected '', got '{result}'"

    # Test 4: Prefix comes after longer word (invalid)
    result = alien_order(["abc", "ab"])
    assert result == "", f"Expected '', got '{result}'"

    # Test 5: Single word
    result = alien_order(["abc"])
    # All characters should appear but order among them is flexible
    assert set(result) == {"a", "b", "c"}, f"Expected set 'abc', got '{result}'"

    # Test 6: Two identical words
    result = alien_order(["z", "z"])
    assert result == "z", f"Expected 'z', got '{result}'"

    print("All tests passed!")
