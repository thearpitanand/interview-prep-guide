"""
Problem: Longest Common Prefix (LC 14) | Day 9 | Easy
Topic: Strings

Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string "".

Example 1:
  Input: strs = ["flower", "flow", "flight"]
  Output: "fl"

Example 2:
  Input: strs = ["dog", "racecar", "car"]
  Output: ""
  Explanation: There is no common prefix among the input strings.

Constraints:
  - 1 <= len(strs) <= 200
  - 0 <= len(strs[i]) <= 200
  - strs[i] consists of only lowercase English letters

Hint: Compare characters at each position across all strings. Stop when
      characters differ or any string is exhausted. Alternatively, sort
      the array and compare only the first and last strings.
Pattern: String Comparison
"""


def longest_common_prefix(strs: list[str]) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix(["", "b"]) == ""
    print("All tests passed!")
