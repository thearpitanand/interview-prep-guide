"""
Problem: Sort Characters By Frequency (LC 451) | Day 13 | Medium
Topic: Searching and Sorting

Given a string s, sort it in decreasing order based on the frequency of the
characters. The frequency of a character is the number of times it appears
in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
  Input: s = "tree"
  Output: "eert" (or "eetr")
  Explanation: 'e' appears twice, 'r' and 't' each appear once.

Example 2:
  Input: s = "cccaaa"
  Output: "aaaccc" (or "cccaaa")

Example 3:
  Input: s = "Aabb"
  Output: "bbAa" (or "bbaA")
  Explanation: 'b' appears twice, 'A' and 'a' each once. Note case sensitivity.

Constraints:
  - 1 <= s.length <= 5 * 10^5
  - s consists of uppercase and lowercase English letters and digits

Hint: Count character frequencies with a hash map, then sort characters by
      frequency in descending order.
Pattern: Hash Map + Sort
"""


def frequency_sort(s: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result1 = frequency_sort("tree")
    assert sorted(result1) == sorted("tree")
    assert result1[:2] == "ee"  # 'e' must come first (highest freq)

    result2 = frequency_sort("cccaaa")
    assert sorted(result2) == sorted("cccaaa")
    assert result2 in ["aaaccc", "cccaaa"]

    result3 = frequency_sort("Aabb")
    assert result3[:2] == "bb"

    print("All tests passed!")
