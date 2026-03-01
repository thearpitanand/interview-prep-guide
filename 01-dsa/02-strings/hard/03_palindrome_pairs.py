"""
Problem: Palindrome Pairs (LC 336) | Day 11 | Hard
Topic: Strings

You are given a 0-indexed array of unique strings words. A palindrome pair
is a pair of indices (i, j) such that:
  - 0 <= i, j < len(words)
  - i != j
  - words[i] + words[j] (the concatenation) is a palindrome

Return a list of all the palindrome pairs.

Example 1:
  Input: words = ["abcd", "dcba", "lls", "s", "sssll"]
  Output: [[0, 1], [1, 0], [3, 2], [2, 4]]
  Explanation:
    "abcd" + "dcba" = "abcddcba" (palindrome)
    "dcba" + "abcd" = "dcbaabcd" (palindrome)
    "s" + "lls" = "slls" (palindrome)
    "lls" + "sssll" = "llssssll" (palindrome)

Example 2:
  Input: words = ["bat", "tab", "cat"]
  Output: [[0, 1], [1, 0]]

Constraints:
  - 1 <= len(words) <= 5000
  - 0 <= len(words[i]) <= 300
  - words[i] consists of lowercase English letters

Hint: Build a hash map of word -> index. For each word, check all possible
      splits. If the left part is a palindrome and the reverse of the right
      part exists in the map, then [reverse_right_index, current_index] forms
      a palindrome pair. Similarly check the right part. Handle the empty
      string case and avoid duplicate pairs.
Pattern: Trie/Hash
"""


def palindrome_pairs(words: list[str]) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
    result_set = {tuple(pair) for pair in result}
    expected_set = {(0, 1), (1, 0), (3, 2), (2, 4)}
    assert result_set == expected_set

    result2 = palindrome_pairs(["bat", "tab", "cat"])
    result_set2 = {tuple(pair) for pair in result2}
    expected_set2 = {(0, 1), (1, 0)}
    assert result_set2 == expected_set2

    result3 = palindrome_pairs(["a", ""])
    result_set3 = {tuple(pair) for pair in result3}
    expected_set3 = {(0, 1), (1, 0)}
    assert result_set3 == expected_set3

    print("All tests passed!")
