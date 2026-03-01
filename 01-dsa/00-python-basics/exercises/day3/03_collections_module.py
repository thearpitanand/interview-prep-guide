"""
Exercise: Collections Module | Day 3
Topic: Python collections

Practice Counter, defaultdict, and deque.

Instructions: Implement each function below.
"""

from collections import Counter, defaultdict, deque


def top_k_frequent(words: list[str], k: int) -> list[str]:
    """Return the k most frequent words.
    Example: top_k_frequent(["a","b","a","c","a","b"], 2) -> ["a", "b"]
    """
    pass


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other.
    Use defaultdict. Return sorted groups (each group sorted).
    Example: group_anagrams(["eat","tea","tan","ate","nat","bat"])
    -> [["ate","eat","tea"], ["bat"], ["nat","tan"]]
    """
    pass


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """Return max of each sliding window of size k using deque.
    Example: sliding_window_max([1,3,-1,-3,5,3,6,7], 3)
    -> [3,3,5,5,6,7]
    """
    pass


def first_unique_char(s: str) -> int:
    """Return index of first non-repeating character.
    Return -1 if none. Use Counter.
    Example: first_unique_char("leetcode") -> 0
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert top_k_frequent(["a", "b", "a", "c", "a", "b"], 2) == ["a", "b"]

    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result = [sorted(g) for g in result]
    result.sort()
    assert result == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    assert first_unique_char("leetcode") == 0
    assert first_unique_char("aabb") == -1
    print("All tests passed!")
