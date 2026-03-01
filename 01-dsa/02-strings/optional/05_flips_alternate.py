"""
Problem: Number of Flips for Alternate Binary String (GFG) | Optional | Easy
Topic: Strings

Given a binary string, find the minimum number of characters to flip to make
it alternating (either "010101..." or "101010...").

Example 1:
  Input: s = "001"
  Output: 1  # flip to "010" or "101" — min 1 flip

Constraints:
  - 1 <= len(s) <= 10^5

Hint: Compare with both patterns "010101..." and "101010...", pick min flips.
Pattern: Greedy
"""


def min_flips_alternate(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_flips_alternate("001") == 1
    assert min_flips_alternate("0001010111") == 2
    assert min_flips_alternate("01") == 0
    print("All tests passed!")
