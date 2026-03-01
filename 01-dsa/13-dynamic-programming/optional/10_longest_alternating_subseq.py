"""
Problem: Longest Alternating Subsequence (GFG) | Optional | Medium
Topic: Dynamic Programming

Find the length of the longest subsequence that alternates between
increasing and decreasing.

Example 1:
  Input: arr = [1, 5, 4]
  Output: 3

Constraints:
  - 1 <= n <= 10^5

Hint: Track two states: last was up, last was down. Greedy: count direction changes + 1.
Pattern: DP / Greedy
"""


def longest_alternating(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_alternating([1, 5, 4]) == 3
    assert longest_alternating([1, 2, 3, 4]) == 2
    assert longest_alternating([10, 22, 9, 33, 49, 50, 31, 60]) == 6
    print("All tests passed!")
