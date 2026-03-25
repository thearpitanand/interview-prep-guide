"""
Exercise: Counter & defaultdict | Day 5
Topic: collections.Counter and collections.defaultdict

Practice using Counter and defaultdict for common patterns.

Instructions: Implement each function below.
"""

from collections import Counter, defaultdict


def top_k_frequent(words: list[str], k: int) -> list[str]:
    """Return the k most frequent words using Counter.most_common().
    Example: top_k_frequent(["a","b","a","c","a","b"], 2) -> ["a", "b"]
    """
    pass


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other using defaultdict(list).
    Sort each group, then sort all groups by their first element.
    Example: group_anagrams(["eat","tea","tan","ate","nat","bat"])
    -> [["ate","eat","tea"], ["bat"], ["nat","tan"]]
    """
    pass


def counter_intersection(s1: str, s2: str) -> dict:
    """Return common characters with their minimum counts using Counter & operator.
    Example: counter_intersection("aabbc", "abccc") -> {'a': 1, 'b': 1, 'c': 1}
    """
    pass


def build_adjacency_list(edges: list[tuple[int, int]]) -> dict[int, set[int]]:
    """Build an undirected graph adjacency list using defaultdict(set).
    Each edge (u, v) means u connects to v AND v connects to u.
    Example: build_adjacency_list([(1,2), (1,3), (2,3)])
    -> {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
    """
    pass


def can_construct(ransom: str, magazine: str) -> bool:
    """Return True if ransom note can be constructed from magazine letters.
    Each letter in magazine can only be used once. Use Counter subtraction.
    Example: can_construct("aa", "aab") -> True
    Example: can_construct("aa", "ab") -> False
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert top_k_frequent(["a", "b", "a", "c", "a", "b"], 2) == ["a", "b"]

    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result = [sorted(g) for g in result]
    result.sort()
    assert result == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    assert dict(counter_intersection("aabbc", "abccc")) == {"a": 1, "b": 1, "c": 1}
    assert dict(counter_intersection("abc", "xyz")) == {}

    adj = build_adjacency_list([(1, 2), (1, 3), (2, 3)])
    assert adj[1] == {2, 3}
    assert adj[2] == {1, 3}
    assert adj[3] == {1, 2}

    assert can_construct("aa", "aab") == True
    assert can_construct("aa", "ab") == False

    print("All tests passed!")
